# LLM Prompting

## Universal Prompting Rules
> LLMs are next-token predictors aligned via instruction tuning. These rules work because they shape the conditional probability distribution the model samples from.

## 1) State the goal first
- **Why it works:** Early tokens set the trajectory (position/recency priors). A clear first sentence collapses the space of plausible continuations toward the intended task.
- **Prevents:** Wandering answers, generic intros.

## 2) Constrain the output (format, length, tone, audience)
- **Why:** Constraints reduce entropy by narrowing valid continuations; schemas mirror learned instruction-tuning patterns (“Return JSON with keys …”).
- **Prevents:** Format drift, verbosity, missing fields.

## 3) Supply minimal but sufficient context (and name it)
- **Why:** Attention is finite; irrelevant tokens cause attention dilution. Labeling scope (“Use only the brief below”) triggers learned context-scoping behavior.
- **Prevents:** Hallucinations, leakage from general knowledge.

## 4) Show 1–2 gold examples (few-shot)
- **Why:** In-context learning induces a local task prior (style, granularity, fields). Examples outperform vague prose rules.
- **Prevents:** Wrong style/level, misread task.

## 5) Decompose hard tasks (plan → draft → refine)
- **Why:** Shorter dependency chains fit working memory better and align with common training patterns (outline → section → polish).
- **Prevents:** Early logical errors compounding.

## 6) Ask for self-checks (without free-form chain-of-thought)
- **Why:** Checklists and “verify before final” motifs are learned patterns; explicit criteria improve calibration without needing hidden reasoning.
- **Prevents:** Missed edge cases, overconfidence.

## 7) Prefer structured thinking (headings, lists, fields)
- **Why:** Structure acts like a soft grammar, supplying latent program flow so the model predicts the next field/step instead of inventing structure.
- **Prevents:** Rambling, skipped steps.

## 8) Control variability (temperature/top-p + schemas)
- **Why:** Lower temperature/top-p concentrates mass on high-probability tokens; schemas further constrain decoding paths for repeatability.
- **Prevents:** Flaky automation, inconsistent results.

## 9) Budget tokens
- **Why:** Long prompts increase distraction, truncation risk, and competition for attention. Salient, concise cues boost signal-to-noise.
- **Prevents:** Ignored key details, context cutoffs.

## 10) Evaluate iteratively with a rubric
- **Why:** External, explicit criteria act like a gradient-free objective; precise deltas steer the model’s outputs in predictable directions.
- **Prevents:** Vague “be better” re-prompts.

## 11) Be safety-aware; request grounding/citations when facts matter
- **Why:** When internal evidence is weak, the model fills gaps with plausible tokens. Asking for sources shifts it into retrieval/justification modes it has learned.
- **Prevents:** Confident but ungrounded claims.

## 12) Decouple from any single provider
- **Why:** Despite alignment quirks, all models are conditional language models. Making task logic, examples, and formatting explicit yields portable priors.
- **Prevents:** Silent regressions when swapping models.

---

### Pocket Mental Model
- **Prompts = constraints on a probability distribution**  
- **Examples = local priors**  
- **Structure = soft grammar**  
- **Decomposition = shorter reasoning paths**  
- **Evaluation loops = external objective**
