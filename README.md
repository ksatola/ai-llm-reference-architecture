# ai-llm-reference-architecture

version 0.0.3

## Topics
- [AI/ML Project Feasibility Study](./Feasibility_Study.md)
- [FTI Architecture](./FTI_Architecture.md)
- [How LLMs Actually Work](./How_LLMs_Work.md)
- [AI Agents, Agentic AI Systems, Agentic Design Patterns](./Agents.md)
- [Model Context Protocol (MCP)](./MCP.md)
- [Universal Prompting Rules](./Prompting.md)
- [Dictionary of terms used in AI](./Dictionary.md)

## AI Projects, Prototypes, Examples
- [MLOps Training Metarials](https://github.com/ksatola/cerebro-agh)
- [LLMs evaluation with another LLM-as-a-judge](./examples/LLM_evaluation_with_LLM_as_a_judge.ipynb) - In this project multiple LLM models are evaluated against a difficult task defined autonomously by another LLM model. The results are cross-evaluated by all models taking part in the comparison and averaged scores are presented. Models examined included: OpenAI GPT, Anthropic Claude, Google Gemini, Deepseek, Groq Llama. There was Mistral model run locally for comparison with Ollama service. This kind of workflow can be used commercially to assess best LLM models for specific job.
- [AI Assistant](https://github.com/ksatola/ai-llm-agent-example) - By themselves, LLMs can't take actions - they just output text. Agents are systems that take a high-level task and use an LLM as a reasoning engine to decide what actions to take and execute those actions. After executing actions, the results can be fed back into the LLM to determine whether more actions are needed, or whether it is okay to finish. In this example, an agent (AI Assistant) can have conversations with its users (humans or other agents). It can provide up-to-date information about the present that the LLM does not possess because it was not trained on it. The agent interacts with a search engine (an external tool) to answer users' questions. The search engine is called Tavily and provides a web search API that enables real-time information retrieval from the internet. It's useful for grounding LLMs with fresh, factual, and search-based answers. The agent has conversational memory - meaning that it can be used as a multi-turn chatbot. The agent remembers past interactions across multiple turns of a conversation which in turn enables context-aware decision-making and more natural, coherent dialogue over time.
- [Twin Writer - AI LLM System Architecture Review](https://github.com/ksatola/ai-llm-twin-writer)
- [AI Career Alter Ego](https://github.com/ksatola/ai-career-alter-ego) - A chat for anyone to interact with to answer all possible questions regarding my career, skills and experience. This AI application uses low level OpenAI client and implements tools constructed from scratch. Apart from an LLM interacting with a human user, this AI application uses another LLM for the first LLM's answers evaluation (using the agentic AI patterns called evaluator-optimizer), as well as various resources and tools. As part of the solution, there is CI/CD workflow configured using Github Actions to deploy the AI app automatically to [Hugging Face Spaces](https://huggingface.co/spaces/ksatola/career_chat) upon successful Github PR merge.
- [Email (generation, evaluation and sending) process automation with AI](./examples/Email_process_automation_with_AI.ipynb) - There are two AI manager actors in this agentic AI workflow: Sales Manager and Email Manager. The first one evaluates and approves the best email content proposed by various AI agents (sales representatives with different characteristics) and hands it over to the second manager handling best email subject generation, email body HTML formatting and sending. The workflow prototype is built using OpenAI Agents SDK demonstrating agents, traces, tools, handoffs and guardrails SDK components in action. It is immediately applicable to Sales Automation; but more generally this could be applied to end-to-end automation of any business process through conversations and tools.
- [Deep Research with AI](https://github.com/ksatola/ai-deep-research) - An AI assistent able to go off, search the internet and do some research on a given topic. This agentic AI workflow has the following steps: ask clarifying questions, plan the search execution, perform searches, write report, evaluate report, optimize report, and send email with the final optimized report. The solution is based on OpenAI Agents SDK and Resend REST API for sending emails.
- [AI Debate](./examples/crewai_debate) - Two agents provide arguments for and against a motion and a third one judges which one is more convincing. This is a simplistic workflow example of using CrewAI framework. See [README.md](./examples/crewai_debate/README.md) for more details.
- [Financial Researcher](./examples/crewai_financial_researcher) - Using sequential process, SERP API as a tool, a financial researcher agent provides inputs to the market analyst to create up-to-date finacial report regaring a chosen company. Built with CrewAI and SERP API powered by Google Search.
- [Stock Picker](./examples/crewai_stock_picker) - Using trending company finder, financial researcher, stock picker and manager (heriarchical process) agents, structured outputs, custom (Pushover for push notifications) and SERP API tools to pick a company for investement in a specified sector. It also uses RAG vector and SQL stores to provide additional context to prompt and to ensure different companies are selected each time. Built with CrewAI.
- [Developer Agent](XXXXXXXXX) - This Coder Agents workflow has ability to write code for specified assignment, execute it in a Docker container, and investigate the results. Built with CrewAI's dockerized code execution capabilities.
- [AI Engineering Team](XXXXXXXXX) - Given requirements, four agents playing common roles in a software development team: engineering lead, frontend developer, backend developer and test engineer build a complete and working solution (a web python-based application). The steps include application design, backend and frontent components development (a single Gradio UI Python module) and then create unit tests. The app is being executed by the AI Engineering Team in a Docker container to confirm that it is working and tested against unit tests. The code comes with verbose comments explaining line by line what is happening. Built with CrewAI.


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
- [SenGrid](https://sendgrid.com/en-us)
- [Resend](https://resend.com/)

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
- [SERP AI](https://serper.dev/) - A low-cost Google Search (SERP - Search Engine Results Page) API that returns structured results (organic links, answer boxes, knowledge panels, etc.) from Google across web, Images, News, Maps/Places, Videos, Shopping, Scholar, and more. It advertises 2,500 free queries and pricing starting around $0.30 per 1,000 queries.


### AI Platforms, Environments, Frameworks
- [OpenAI](https://platform.openai.com/)
- [ANTHROP\C](https://www.anthropic.com/)
- [CrewAI ](https://www.crewai.com/)

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
- [CrewAI UI Studio](https://github.com/strnad/CrewAI-Studio) - A no-code / low-code product for creating multi-agent solutions.
- [OpenAI Agent Builder](https://platform.openai.com/docs/guides/agent-builder) - A visual canvas for building multi-step agent workflows.
- [Google AI Studio](https://aistudio.google.com/)


### Online Education, Books
- [Master and Build Large Language Models by Sebastian Raschka](https://www.manning.com/livevideo/master-and-build-large-language-models)


### Selected Newsletters, Articles, Online Publications, Infographics
- [Daily Dose of Data Science](https://www.dailydoseofds.com/)
  - [A Beginner-friendly and Comprehensive Deep Dive on Vector Databases](https://www.dailydoseofds.com/a-beginner-friendly-and-comprehensive-deep-dive-on-vector-databases)



## To review
- [Building Business-Ready Generative AI Systems: Build Human-Centered AI Systems with Context Engineering, Agents, Memory, and LLMs for Enterprise](https://www.packtpub.com/en-us/product/building-business-ready-generative-ai-systems-9781837020683)
