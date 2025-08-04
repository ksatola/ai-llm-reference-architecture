# Model Context Protocol (MCP)

**Model context protocol (MCP)** is an open standard proposed by [Anthrop\c](https://www.anthropic.com/) that enables developers to build secure, two-way connections between their data sources and AI-powered tools. Open technologies like the Model Context Protocol are the bridges that connect AI to real-world applications, ensuring innovation is accessible, transparent, and rooted in collaboration.

![Source: https://www.dailydoseofds.com/](/images/mcp_01.png)

MCP was developed to:
- Provide a protocol for seamless integration between LLM applications and external data sources.
- Replace fragmented integrations with a single protocol.
- Make truly connected systems simpler and easier to scale.
- Allow better collaboration between Client/Server developers and systems they develop.


## MCP Architecture Overview
The architecture is straightforward: developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers.


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
- [Model Context Protocol Specification](https://modelcontextprotocol.io/overview)
- [Model Context Protocol Gihub repository](https://github.com/modelcontextprotocol)
- [Model Context Protocol servers reference implementation](https://github.com/modelcontextprotocol/servers)
- [MCP - The Illustrated Guidebook from DailyDoseofDS.com](https://www.dailydoseofds.com/)
