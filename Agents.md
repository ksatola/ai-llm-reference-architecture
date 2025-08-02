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

### Prompt chaining

**Prompt chaining** decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_workflow_patterns_01.png)

#### When to use this workflow
This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

#### Examples where this workflow is useful
- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Routing

**Routing** classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs. Classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_workflow_patterns_02.png)

#### When to use this workflow
Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately.

#### Examples where this workflow is useful
- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller models like Claude 3.5 Haiku and hard/unusual questions to more capable models like Claude 3.5 Sonnet to optimize cost and speed.

### Parallelization

**Parallelization**. LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:
- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting**: Running the same task multiple times to get diverse outputs.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_workflow_patterns_03.png)

#### When to use this workflow
Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

#### Examples where this workflow is useful
- Sectioning:
    - Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response.
    - Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model’s performance on a given prompt.
- Voting:
    - Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
    - Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.

### Orchestrator-workers

**Orchestrator-workers** - a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_workflow_patterns_04.png)

#### When to use this workflow
This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

#### Examples where this workflow is useful
- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Evaluator-optimizer

**Evaluator-optimizer** - one LLM call generates a response while another provides evaluation and feedback in a loop.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_workflow_patterns_05.png)

#### When to use this workflow
This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

#### Examples where this workflow is useful
- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.
- 

## Agents
- Agents begin their work with either a command from, or interactive discussion with, the human user. 
- Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. 
- Agents can then pause for human feedback at checkpoints or when encountering blockers. 
- The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_02.png)

### When to use agents
Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. It is recommended to perform extensive testing in sandboxed environments, along with the appropriate guardrails.

### Examples where agents are useful
- A customer support representative combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because:
    - Support interactions naturally follow a conversation flow while requiring access to external information and actions.
    - Tools can be integrated to pull customer data, order history, and knowledge base articles.
    - Actions such as issuing refunds or updating tickets can be handled programmatically.
    - Success can be clearly measured through user-defined resolutions.
- A coding Agent supporting a software developer with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because:
  - Code solutions are verifiable through automated tests.
  - Agents can iterate on solutions using test results as feedback.
  - The problem space is well-defined and structured.
  - Output quality can be measured objectively.
- A [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

![Source: https://www.anthropic.com/engineering/building-effective-agents](/images/agentic_ai_03.png)


## Summary
The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity only when it demonstrably improves outcomes.

Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

Try to follow three core principles:
1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent’s planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

## References
- [Building effective agents by Anthropic](https://www.anthropic.com/engineering/building-effective-agents)
- [Building Effective Agents Cookbook](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
