# ai-llm-reference-architecture

version 0.0.2






## Resources


### Specifications
- [Model Context Protocol](https://github.com/modelcontextprotocol)


### Tools
- [What-If-Tool (WIT)](https://pair-code.github.io/what-if-tool/)
- [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard)
- [Tensorflow Playground](https://playground.tensorflow.org/)
- [Diagrams.net](https://app.diagrams.net/)
- [UV Python package manager](https://github.com/astral-sh/uv), [docs](https://docs.astral.sh/uv/)
- [gradio for building shareable web UIs](https://www.gradio.app/)
- [Pushover for simple notifications](https://pushover.net/)
- [Hugging Face Spaces](https://huggingface.co/)

```
uv init
uv --version
uv add gradio openai
uv sync
uv export -o requirements.txt
uv export --format requirements-txt --no-hashes -o requirements.txt
uv run python_script.py
uv python list
```

- [Cursor AI-powered IDE](https://cursor.com/)


### AI Platforms, Environments
- [OpenAI](https://platform.openai.com/)
- [ANTHROP\C](https://www.anthropic.com/)
- [Google AI Studio](https://aistudio.google.com/)
- [deepseek](https://www.deepseek.com/en)
- [groq](https://groq.com/)
- [Ollama (run LLMs locally)](https://ollama.com/)


### Agentic AI Frameworks
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)
- [Crew AI]()
- [LangGraph]()
- [Microsoft AutoGen]()
- [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- [n8n (low code Agentic AI platform)](https://n8n.io/)


### Online Education, Books
- [Master and Build Large Language Models by Sebastian Raschka](https://www.manning.com/livevideo/master-and-build-large-language-models)


### Newsletters, Articles, Online Publications, Infographics
- [Daily Dose of Data Science](https://www.dailydoseofds.com/)
  - [A Beginner-friendly and Comprehensive Deep Dive on Vector Databases](https://www.dailydoseofds.com/a-beginner-friendly-and-comprehensive-deep-dive-on-vector-databases)


## AI Projects, Examples
- [MLOps Training Metarials](https://github.com/ksatola/cerebro-agh)
- [LLMs evaluation with another LLM as a judge](./examples/LLM_evaluation_with_LLM_as_a_judge.ipynb)
- [AI Agent Example](https://github.com/ksatola/ai-llm-agent-example)
- [Twin Writer - AI LLM System Architecture Review](https://github.com/ksatola/ai-llm-twin-writer)
- [AI Career Alter Ego](https://github.com/ksatola/ai-career-alter-ego) - A chat for anyone to interact with to answer all possible questions regarding my career, skills and experience. This AI application uses low level OpenAI client and implements tools constructed from scratch. Apart from an LLM interacting with a human user, this AI application uses another LLM for the first LLM's answers evaluation (using the agentic AI patterns called evaluator-optimizer), as well as various resources and tools. As part of the solution, there is CI/CD workflow configured using Github Actions to deploy the AI app automatically to [Hugging Face Spaces](https://huggingface.co/spaces/ksatola/career_chat) upon successful Github PR merge.
- [Email (generation, evaluation and sending) process automation with AI](XXXXXXXXXX) - There are two AI manager actors in this AI workflow: Sales Manager and Email Manager. The first one evaluates and approves the best email content proposed by various AI agents (sales representatives with different characteristics) and hands it over to the second manager handling best email subject generation, email body HTML formatting and sending. This AI workflow prototype is built using OpenAI Agents SDK demonstrating agents, traces, tools and handoffs SDK components in action. It is immediately applicable to Sales Automation; but more generally this could be applied to end-to-end automation of any business process through conversations and tools.


## For Further Processing




## To review
- [Building Business-Ready Generative AI Systems: Build Human-Centered AI Systems with Context Engineering, Agents, Memory, and LLMs for Enterprise](https://www.packtpub.com/en-us/product/building-business-ready-generative-ai-systems-9781837020683)
