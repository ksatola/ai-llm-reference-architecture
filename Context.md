# Context

In AI systems, context refers to the additional information or surrounding data that helps the system understand, interpret, or respond more accurately to a given input or task.

Think of it as the "situation" or "background" in which the AI is operating — without context, even a powerful model can misunderstand or behave inappropriately.

Context in AI systems is all the surrounding or historical information that helps the AI system better understand, interpret, and act appropriately in a given situation. It’s essential for building AI that is coherent, relevant, and intelligent in complex or dynamic tasks.

## Types of Context in AI

| Type                      | Description                                                            |
| ------------------------- | ---------------------------------------------------------------------- |
| **Conversation history**  | Prior messages in a chat or dialogue (used in LLMs like ChatGPT)       |
| **User data/profile**     | User preferences, history, goals, location, device info                |
| **Task-specific info**    | Instructions, current goal, system state, or app-specific data         |
| **Environmental context** | Sensor input, time, weather, nearby devices (common in robotics/IoT)   |
| **Domain knowledge**      | Knowledge base or rules relevant to a specific domain (e.g., medicine) |
| **Retrieved documents**   | Factual references retrieved before answering (as in RAG systems)      |

## Why Context Matters

Without context, AI systems can:
- Misunderstand vague inputs (e.g., "Can you do it?" → What is “it”?)
- Give irrelevant or incorrect answers (e.g., "Add more RAM" → for a shopping site or a laptop review?)
- Lose track of conversation state (e.g., Repeating answers in a chat)

With context, AI systems can:
- Stay on topic
- Disambiguate meaning
- Personalise responses
- Act intelligently in a broader environment

## Examples in Practice

- LLMs (e.g., GPT-4, Claude)
  - Use prompt context (everything you’ve typed in the chat)
  - Can also use retrieval context (RAG: retrieving relevant documents)

- AI Assistants (e.g., Alexa, Siri)
  - Use user intent, past interactions, device location, etc.

- Autonomous Agents / Agentic AI
  - Use task memory, intermediate states, and tools used to adapt actions over time

## Limits of Context

- LLMs have context window limits (e.g., 128K tokens max).
- Forgetting happens when info falls outside the window. 
- Adding too much context can also confuse or dilute attention.
