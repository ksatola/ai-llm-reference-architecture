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
- **MCP Server** is an external program or service that provides the capabilities (tools, data, etc.) to the application. Server advertises what it can do in a standard format (so clients can query and understand available tools) and executes requests coming from clients, then return results.

![Source: https://www.dailydoseofds.com/](/images/mcp_02.png)

## MCP Core Capabilities

Tools, prompts and resources form the three core capabilities of the MCP framework:
- **Tools** are executable actions or functions that the AI (host/client) can invoke (often with side effects or external API calls). Tools are usually triggered by the AI model’s choice, which means the LLM (via the host) decides to call a tool when it determines it needs that functionality.
- **Resources** are read-only data sources that the AI (host/client) can query for information (no side effects, just retrieval).
- **Prompts** are predefined prompt templates or workflows that servers can supply.



## References
- [MCP - The Illustrated Guidebook from DailyDoseofDS.com](https://www.dailydoseofds.com/)
