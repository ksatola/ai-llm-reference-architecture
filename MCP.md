# Model Context Protocol (MCP)

**Model context protocol (MCP)** is a standardized interface and framework that allows AI models to seamlessly interact with external tools, resources, and environments.

![Source: https://www.dailydoseofds.com/](/images/mcp_01.png)

MCP was developed to:
- Provide Structured, Persistent Context for Agents. LLMs like GPT are stateless: they don’t "remember" past interactions unless the entire history is sent again. MCP provides a structured way to maintain, manage, and update context between prompts, allowing agents to have memory and continuity in reasoning.
- Enable Modular and Interoperable Agent Design. Agentic systems often have multiple components: planner, executor, retriever, memory store, etc. MCP standardises how these components communicate, making it easier to swap models or tools while maintaining a shared context.
- Manage Complex Contexts Beyond Prompt Windows. With limited token windows, agents need to prioritise, compress, and retrieve context efficiently. MCP supports context chunking, tagging, and relevance scoring to decide what information to include in prompts.
- Support Multi-Agent Collaboration. In systems with multiple agents working together (e.g., agent collectives), there needs to be a shared context or protocol for exchanging memory and goals. MCP acts as the protocol layer that supports coordination.
- Facilitate Agent Autonomy and Planning. Agents need to store goals and tasks, reflect on past actions, and plan ahead. MCP structures this episodic memory, goal state, and task history to help the agent reason more autonomously.

## MCP Architecture Overview

MCP follows a client-server architecture with the three main roles: Host, Client, and Server.
- **MCP Host** is a user-facing AI application, an environment where the AI model lives and interacts with a user. Host initiates connections to the available MCP servers when the system needs them. It captures the user's input, keeps the conversation history, and displays the model’s replies.
- **MCP Client** is a component within the Host that handles the low-level communication with an MCP Server. While Host decides what to do, Client knows how to speak MCP to carry out those instructions with the server.
- **MCP Server** is an external program or service that provides the capabilities (tools, context and prompt templates) to the application (Host). Server advertises what it can do in a standard format (so clients can query and understand available tools) and executes requests coming from clients, then return results.

![Source: https://www.dailydoseofds.com/](/images/mcp_02.png)

## MCP Core Capabilities

Tools, prompts and resources form the three core capabilities of the MCP framework:
- **Tools** are executable actions or functions that the AI (host/client) can invoke (often with side effects or external API calls). Tools are usually triggered by the AI model’s choice, which means the LLM (via the host) decides to call a tool when it determines it needs that functionality. Tools are registered with metadata (e.g. name, description, expected input/output types). The agent uses tools via a function-calling interface or tool selection reasoning step. Tool usage is tracked in context memory, including result summaries and relevance.
- **Resources** are read-only data sources (long-term knowledge or assets) that the AI (host/client) can query for information (no side effects, just retrieval). Unlike tools, resources typically do not involve heavy computation or side effects, since they are often just information lookup. Resources are usually accessed under the host application’s control (not spontaneously by the model). In practice, this might mean the Host knows when to fetch a certain context for the model. Resources are often indexed in a vector store or database, or retrieved via similarity search or relevance scoring.
- **Prompts** are predefined  or dynamically generated templates or conversation flows that can be injected to guide the AI’s behavior (and Server can supply). Prompt capability provides a canned set of instructions or an example dialogue that can help steer the model for certain tasks. Prompts, as a capability, blur the line between data and instructions.

![Source: none](/images/mcp_03.png)

## References
- [Introducing the Model Context Protocol by Anthropic](https://www.anthropic.com/news/model-context-protocol)
- [MCP - The Illustrated Guidebook from DailyDoseofDS.com](https://www.dailydoseofds.com/)
