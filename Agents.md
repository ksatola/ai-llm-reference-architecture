# AI Agents / Agentic AI Systems

AI Agents are programs where LLM outputs control the workflow.


## Agentic AI
An Agentic AI solution involves any or all off these:
- Multiple LLm calls
- LLMs with ability to use Tools
- An environment where LLMs interact
- A Planner to coordinate activities
- Autonomy

Anthropic distinguishes two types of Agentic Systems:
- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents** are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

The most successful implementations of agentic systems use simple, composable patterns rather than complex frameworks.


## When To (Not) Use Agents
When building applications with LLMs, find the simplest solution possible, and only increase complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.


## When And How To Use Frameworks
There are many frameworks that make agentic systems easier to implement, including:
- LangGraph from [LangChain](https://langchain-ai.github.io/langgraph/).
- [Amazon Bedrock's](https://aws.amazon.com/bedrock/agents/) AI Agent framework.
- [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder.
- [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

## The Augmented LLM
The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_01.png)

## 5 Workflow Design Patterns
1. Prompt chaining - use one or more LLMs in a sequence to decompose your logic into fised sub-tasks.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_workflow_patterns_01.png)

2. Routing - 


## References
- [Building effective agents by Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [Building Effective Agents Cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
