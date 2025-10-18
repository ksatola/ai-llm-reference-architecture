# Model Context Protocol (MCP)

**Model context protocol (MCP)** is an open standard proposed by [Anthrop\c](https://www.anthropic.com/) in late November 2024 that enables developers to build secure, two-way connections between their data sources and AI-powered tools. MCP is open and model-agnostic. This means any AI model (Claude, GPT-4, open-source LLMs, etc.) can use MCP, and any developer or company can create an MCP integration without permission. Open technologies like the Model Context Protocol are the bridges that connect AI to real-world applications, ensuring innovation is accessible, transparent, and rooted in collaboration.

MCP is not an orchestration engine or agent brain by itself. Rather, it’s an integration layer within an agentic architecture. It complements agent orchestration tools like LangChain, LangGraph, CrewAI, or LlamaIndex by serving as a unified "toolbox" from which AI agents can invoke external actions. Instead of replacing orchestration – which determines when and why an agent uses a tool – MCP defines how these tools are called and information exchanged.

![Source: https://www.dailydoseofds.com/](/images/mcp_01.png)

MCP was developed to:
- Provide a protocol for seamless integration between LLM applications and external data sources.
- Replace fragmented integrations with a single protocol.
- Make truly connected systems simpler and easier to scale.
- Allow better collaboration between Client/Server developers and systems they develop.

MCP lays out clear rules for how AI can find, connect to, and use external tools – whether it’s querying a database or running a command. This lets models go beyond their training data, making them more flexible and aware of the world around them.

One striking feature is MCP’s dynamic discovery – AI agents automatically detect available MCP servers and their capabilities, without hard-coded integrations. For example, if you spin up a new MCP server (like a CRM), agents can immediately recognize and use it via a standardized API, offering flexibility traditional approaches can't match.

## MCP Architecture Overview
The architecture is straightforward: developers can either expose their data through MCP servers or build AI applications (MCP clients) that connect to these servers.


MCP follows a client-server architecture with the three main roles: Host, Client, and Server.
- **MCP Host** is a user-facing AI application, an environment where the AI model lives and interacts with a user. Host initiates connections to the available MCP servers when the system needs them. It captures the user's input, keeps the conversation history, and displays the model’s replies.
- **MCP Client** is a connector component within the Host application that handles the low-level communication with an MCP Server. While Host decides what to do, Client knows how to speak MCP to carry out those instructions with the server.
- **MCP Server** is an external program, process or service that provides the capabilities (tools, context and prompt templates) to the application (Host). Can run locally on the same machine or remotely. Server advertises what it can do in a standard format (so clients can query and understand available tools) and executes requests coming from clients, then return results.

![Source: https://www.dailydoseofds.com/](/images/mcp_02.png)

### Communication Layer Protocols
- **Stdio** spawns a process and communicates via standard input/output
- **SSE** uses HTTPS with streaming

![Source: https://www.dailydoseofds.com/](/images/mcp_04.png)

## MCP Core Capabilities

Tools, prompts and resources form the three core capabilities of the MCP framework:
- **Tools** are executable actions or functions that the AI (host/client) can invoke (often with side effects or external API calls). Tools are usually triggered by the AI model’s choice, which means the LLM (via the host) decides to call a tool when it determines it needs that functionality. Tools are registered with metadata (e.g. name, description, expected input/output types). The agent uses tools via a function-calling interface or tool selection reasoning step. Tool usage is tracked in context memory, including result summaries and relevance.
- **Resources** are read-only data sources (long-term knowledge or assets) that the AI (host/client) can query for information (no side effects, just retrieval). Unlike tools, resources typically do not involve heavy computation or side effects, since they are often just information lookup. Resources are usually accessed under the host application’s control (not spontaneously by the model). In practice, this might mean the Host knows when to fetch a certain context for the model. Resources are often indexed in a vector store or database, or retrieved via similarity search or relevance scoring.
- **Prompts** are predefined  or dynamically generated templates or conversation flows that can be injected to guide the AI’s behavior (and Server can supply). Prompt capability provides a canned set of instructions or an example dialogue that can help steer the model for certain tasks. Prompts, as a capability, blur the line between data and instructions.

![Source: none](/images/mcp_03.png)

## MCP Concerns
- MCP **added overhead of managing multiple tool servers**. Running and maintaining connections to these local servers can be cumbersome, particularly in production environments where uptime, security, and scalability are paramount. MCP's initial implementation was designed for local and desktop use, which raises questions about how well it translates to cloud-based architectures and multi-user scenarios. Developers have proposed making MCP more stateless and adaptable to distributed environments, but this remains an ongoing challenge.
- **Tools usability**. Just because MCP expands an AI model’s toolset does not necessarily mean the model will use those tools effectively. Previous agent-based frameworks have demonstrated that AI models can struggle with tool selection and execution. MCP attempts to mitigate this by providing structured tool descriptions and specifications, but success still hinges on the quality of these descriptions and the AI’s ability to interpret them correctly.
- **MCP’s maturity** is also a consideration. As a relatively new technology, it is subject to rapid changes and evolving standards. This can lead to breaking changes, requiring frequent updates to servers and clients. While the core concept of MCP appears stable, developers should anticipate and prepare for version upgrades and evolving best practices.
- **Compatibility** is another limiting factor. Currently, MCP has first-class support within Anthropic’s ecosystem (e.g., Claude), but broader adoption remains uncertain. Other AI providers may not natively support MCP, requiring additional adapters or custom integrations. Until MCP gains wider acceptance across AI platforms, its utility will be somewhat constrained.
- For simpler applications, **MCP may even be overkill**. If an AI model only needs to access one or two straightforward APIs, direct API calls might be a more efficient solution than implementing MCP. The learning curve associated with MCP’s messaging system and server setup means that its benefits need to be weighed against its complexity.
- **Security and monitoring** also present ongoing challenges. Since MCP acts as an intermediary, it necessitates robust authentication and permission controls to prevent unauthorized access. Open-source initiatives like MCP Guardian have emerged to address these concerns by logging requests and enforcing policies, but securing MCP in enterprise environments remains a work in progress.

## New Possibilities Unlocked by MCP
MCP is still new, and its full potential is just being explored. The first wave of use cases is obvious – connecting enterprise data to chat assistants or enhancing coding agents with repository access. But some emerging applications could take AI agents to the next level.
- **Multi-Step, Cross-System Workflows Agentic systems often need to coordinate across platforms**. Say an AI plans an event: it checks your calendar, books a venue, emails guests, arranges travel, and updates a budget sheet.
- **Agents That Understand Their Environment (including Robotics)**. Beyond tool access, MCP can enable AI agents embedded in smart environments – whether in a smart home or an operating system. An AI assistant could interact with sensors, IoT devices, or OS functions via standardized MCP servers. Instead of operating in isolation, the AI gains real-time awareness, enabling more natural and proactive assistance.
- **Collaborating Agents (Agent Societies)**. Specialized AI agents – one for research, one for planning, another for execution – could use MCP to exchange information and coordinate tasks dynamically.
- **Personal AI Assistants with Deep Integration MCP could let users configure their own AI to interact with personal data and apps securely**. A local MCP server could grant an AI access to emails, notes, and smart devices without exposing sensitive data to third parties. This could create an ultra-personalized AI assistant without relying on cloud-based services.
- **Enterprise Governance and Security For businesses**. MCP standardizes AI access to internal tools, reducing integration overhead. It also enables governance: AI interactions can be logged, monitored, and controlled via an oversight layer, preventing unintended actions while maintaining efficiency.


## References
- [Introducing the Model Context Protocol by Anthropic](https://www.anthropic.com/news/model-context-protocol)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/overview)
- [Model Context Protocol Gihub repository](https://github.com/modelcontextprotocol)
- [Model Context Protocol servers reference implementation](https://github.com/modelcontextprotocol/servers)
- [What Is MCP, and Why Is Everyone – Suddenly!– Talking About It?](https://huggingface.co/blog/Kseniase/mcp)
- [TOP 11 Essential MCP Libraries](https://huggingface.co/blog/LLMhacker/top-11-essential-mcp-libraries)
- [MCP - The Illustrated Guidebook from DailyDoseofDS.com](https://www.dailydoseofds.com/)
