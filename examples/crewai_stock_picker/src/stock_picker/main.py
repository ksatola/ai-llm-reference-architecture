#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from stock_picker.crew import StockPicker

import io
import requests
import pandas as pd
import plotly.graph_objects as go
import gradio as gr
from pathlib import Path
import json
from typing import Dict, Any, List

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


_PERIOD_MONTHS = {"1mo":1, "3mo":3, "6mo":6, "1y":12, "2y":24, "5y":60, "10y":120}
_INTERVAL_MAP = {"1d":"d", "1wk":"w", "1mo":"m"}  # Stooq supports only d/w/m

MD_PATH = Path("output/decision.md")

def _stooq_symbol(ticker: str) -> str:
    t = ticker.strip().lower()
    # For typical US tickers Stooq uses e.g. aapl.us, nvda.us
    return (t + ".us") if "." not in t and 1 <= len(t) <= 5 else t

def stock_plot(name="", ticker="", reason="", period="1y", interval="1d", style="line"):
    """
    Stooq-only: fetch OHLC and return a Plotly Figure (ready for gr.Plot).

    Args:
        ticker: e.g., "AAPL", "NVDA" (mapped to aapl.us / nvda.us on Stooq)
        period: one of {"1mo","3mo","6mo","1y","2y","5y","10y","max"}
        interval: one of {"1d","1wk","1mo"} (mapped to Stooq d/w/m)
        style: "line" or "candlestick"
        name: optional display name to show in the chart title
        reason: optional note shown as a subtitle
    """
    if not ticker or not ticker.strip():
        raise ValueError("Provide a ticker, e.g., AAPL or NVDA.")
    if interval not in _INTERVAL_MAP:
        raise ValueError(f"Unsupported interval '{interval}'. Use one of: {list(_INTERVAL_MAP)}")

    sym = _stooq_symbol(ticker)
    url = f"https://stooq.com/q/d/l/?s={sym}&i={_INTERVAL_MAP[interval]}"

    # Fetch text; guard against HTML/error pages
    r = requests.get(url, timeout=15)
    if r.status_code != 200 or not r.text.strip():
        raise ValueError(f"Stooq request failed for {ticker} ({sym}). HTTP {r.status_code}")
    txt = r.text.lstrip()
    if txt.startswith("<"):
        raise ValueError(f"Stooq returned HTML (likely bad symbol '{sym}' or server issue).")

    # Read CSV, normalize headers
    df = pd.read_csv(io.StringIO(txt))
    df.columns = [c.strip().title() for c in df.columns]

    print(df.head())
    print(df.columns)

    if "Date" not in df.columns:
        raise ValueError("Missing 'Date' column in Stooq response (unexpected CSV format).")

    # Clean + trim by period
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"]).sort_values("Date")
    if df.empty:
        raise ValueError(f"No rows returned by Stooq for {ticker} ({sym}).")

    if period != "max":
        months = _PERIOD_MONTHS.get(period, 12)
        cutoff = pd.Timestamp.today().normalize() - pd.DateOffset(months=months)
        df = df[df["Date"] >= cutoff]
        if df.empty:
            raise ValueError(f"No rows for {ticker} within period '{period}' from Stooq.")

    # Build figure
    have_ohlc = all(c in df.columns for c in ["Open","High","Low","Close"])
    title_main = f"{ticker.upper()} • {period} • {interval}"
    #subtitle = "  ".join(s for s in [name.strip(), reason.strip()] if s)
    subtitle = None
    title_text = f"{title_main}<br><sup>{subtitle}</sup>" if subtitle else title_main

    if style == "candlestick" and have_ohlc:
        fig = go.Figure(go.Candlestick(
            x=df["Date"],
            open=df["Open"].astype(float),
            high=df["High"].astype(float),
            low=df["Low"].astype(float),
            close=df["Close"].astype(float),
            name=ticker.upper(),
        ))
    else:
        if "Close" not in df.columns:
            raise ValueError("Stooq data missing 'Close' column.")
        fig = go.Figure(go.Scatter(
            x=df["Date"],
            y=df["Close"].astype(float),
            mode="lines",
            connectgaps=True,
            name=f"{ticker.upper()} Close",
        ))

    fig.update_layout(
        title=title_text,
        xaxis_title="Date",
        yaxis_title="Price",
        hovermode="x unified",
        margin=dict(l=40, r=20, t=50, b=40),
    )
    return fig


# Not used in Gradio app, but here for reference
def read_local_md():
    if not MD_PATH.exists():
        return f"# File not found\n`{MD_PATH.resolve()}`"
    return MD_PATH.read_text(encoding="utf-8")


def run_with_md(name, ticker, reason, period, interval, style, report):
    # 1) make the chart via your existing function
    fig = stock_plot(name, ticker, reason, period, interval, style)

    # 2) read markdown if provided
    if report is None:
        md_text = "*(No markdown file uploaded)*"
    else:
        md_text = read_local_md()
        print(md_text)

    return fig, md_text


def run():
    """
    Run the research crew.
    """
    inputs = {
        'sector': 'Technology',
        "current_date": str(datetime.now())
    }

    # Create and run the crew
    result = StockPicker().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)

    model_obj: StockPicker = result.pydantic
    print(model_obj.model_dump())

    final_recommendation = model_obj.model_dump()
    name = final_recommendation["best_stock"]["name"]
    ticker = final_recommendation["best_stock"]["ticker"]
    reason = final_recommendation["best_stock"]["reason"]
    decision = final_recommendation["final_report_md"]
    print(ticker)
    print(decision)

    # Minimal Gradio app
    demo = gr.Interface(
        fn=run_with_md,
        inputs=[
            gr.Textbox(label="Name", value=name, interactive=False),
            gr.Textbox(label="Ticker", value=ticker),
            gr.Textbox(label="Reason", value=reason, lines=5, interactive=False),
            gr.Dropdown(["1mo","3mo","6mo","1y","2y","5y","10y","max"], value="1y", label="Period"),
            gr.Dropdown(["1d","1wk","1mo"], value="1d", label="Interval"),
            gr.Radio(["line","candlestick"], value="line", label="Style"),
            gr.Textbox(label="Report", value=MD_PATH, interactive=False),
        ],
        outputs=[
            gr.Plot(label="Price Chart"),
            gr.Markdown(label="Final Decision"),
        ],
        title="Stock Picker (CrewAI → Stooq → Plotly → Gradio)",
        flagging_mode="never",
    )

    demo.launch()


if __name__ == "__main__":
    run()
