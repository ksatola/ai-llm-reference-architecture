# LLMs Classes

There are different Large Language Models (LLMs) classes:

## Reasoning Models
An LLM reasoning model is a model that is explicitly trained or designed to perform reasoning tasks—such as logical inference, planning, chain-of-thought problem-solving, or multi-step decision-making.
- Encourages step-by-step thinking ("chain of thought" prompting)
- Handles complex multi-hop questions
- Supports tool use, memory, and reflection (in agentic systems)
- May integrate external context or knowledge retrieval (like RAG)

Multi-step logic & planning
- Focus: Planning, problem-solving, logic, multi-step inference
- Examples: GPT-4 with CoT, ReAct, DeepMind’s AlphaCode, Toolformer

## Retrieval-Augmented Models
A Retrieval-Augmented Model (often abbreviated as RAG: Retrieval-Augmented Generation) is a type of Large Language Model (LLM) system that combines language generation with external knowledge retrieval. A Retrieval-Augmented Model lets LLMs “look things up” rather than just “make things up.”
It’s a hybrid of search and generation — enabling more accurate, contextual, and up-to-date AI applications.

LLMs like GPT, Claude, or LLaMA are trained on vast amounts of data—but:
- Their knowledge is frozen at training time
- They have a limited context window (i.e., how much you can fit in a prompt)
- They can hallucinate facts if unsure

Retrieval-Augmented Models solve this by injecting real, up-to-date, and relevant information into the model at runtime, not just during training.

External knowledge integration
- Use external knowledge (RAG) to extend their context window (prompt)
- Examples: OpenAI + vector store (e.g. via LangChain), Bing Chat

## Instruction-Tuned Models
An LLM instruction-tuned model is a Large Language Model that has been fine-tuned to follow human-written instructions effectively. This makes the model more useful, responsive, and aligned with user intent — especially in tasks like answering questions, generating summaries, writing code, or following multi-step tasks. An instruction-tuned LLM is trained to be a versatile assistant. It doesn’t just generate text — it follows human commands accurately, often with little or no example.

Instruction tuning is a process where a pretrained LLM (like GPT or T5) is further trained on datasets of (instruction, input, output) examples to teach it how to follow specific commands or tasks described in natural language.

| Feature                  | Benefit                                          |
| ------------------------ | ------------------------------------------------ |
| **Task generalisation**  | Performs well on unseen tasks with just a prompt |
| **Improved alignment**   | Understands what users *want* better             |
| **Fewer hallucinations** | Generates more relevant and coherent output      |
| **Natural UX**           | Users can just “ask” without formatting or code  |

| Model                | Base Model | Description                                                                          |
| -------------------- | ---------- | ------------------------------------------------------------------------------------ |
| **FLAN-T5**          | T5         | Google's model trained on 1000+ instructions                                         |
| **InstructGPT**      | GPT-3      | OpenAI's version of GPT-3 fine-tuned to follow instructions (predecessor of ChatGPT) |
| **ChatGPT**          | GPT-3.5/4  | Trained with instruction + reinforcement                                             |
| **Alpaca**           | LLaMA      | Lightweight model trained on instruction pairs                                       |
| **Dolly**            | GPT-J      | Instruction-tuned on Databricks-generated data                                       |
| **Mistral-Instruct** | Mistral    | Small, efficient instruction-tuned model                                             |

Following user prompts well
- Trained to follow user instructions
- Examples: FLAN-T5, OpenAssistant, Dolly, Alpaca

## Chat Models / Dialogue Models
An LLM Chat / Dialogue Model is a Large Language Model fine-tuned or architected specifically for multi-turn conversations with humans. These models are designed not just to generate accurate or informative text, but also to maintain coherence, context, tone, and persona across an interactive dialogue. A chat or dialogue model is an LLM specialised for interactive, multi-turn conversations that are helpful, natural, and context-aware. It’s what powers AI assistants, customer service bots, and collaborative creative tools.

Unlike general LLMs that generate one-off completions or summaries, chat models are trained to:
- Remember prior conversation turns
- Respond in a polite, helpful, and safe manner
- Support follow-ups and clarifications
- Adopt a consistent persona or tone (e.g. helpful assistant, friendly tutor)

| Capability               | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Memory of turns**      | Remembers what was said earlier in the chat         |
| **Contextual awareness** | Adjusts responses based on conversation flow        |
| **Tone adaptation**      | Can be formal, casual, humorous, etc.               |
| **Persona consistency**  | Can maintain a role (e.g. doctor, tutor, assistant) |
| **Safety filters**       | Avoids harmful or sensitive content                 |

| Model                | Notes                                                         |
| -------------------- | ------------------------------------------------------------- |
| **ChatGPT**          | GPT-3.5/4 with RLHF, one of the most advanced dialogue agents |
| **Claude**           | Anthropics’s helpful, honest, and harmless model              |
| **Gemini**           | Google's multimodal conversational model                      |
| **LLaMA-2 Chat**     | Meta’s fine-tuned open-source chat variant                    |
| **Mistral-Instruct** | Optimised for dialogue-like completions                       |
| **Vicuna, Alpaca**   | Open-source chatbots trained on ChatGPT-style data            |

Safe, engaging conversation
- Optimised for natural, safe, helpful conversation
- Examples: ChatGPT, Claude, Gemini

## Code Models
An LLM Code Model is a Large Language Model that has been trained or fine-tuned specifically to understand, generate, and reason about programming code. These models are used in code completion, debugging, documentation, translation between languages, and even generating entire software components. An LLM Code Model is a language model purpose-built to read, write, and understand source code in multiple programming languages. It powers tools like GitHub Copilot, ChatGPT code interpreter, and AI pair programmers.

Unlike general LLMs trained on web text and books, code models are trained on:
- Source code in multiple languages (e.g. Python, JavaScript, C++)
- Code documentation (e.g. docstrings, comments)
- StackOverflow/Q&A data
- GitHub repos, Jupyter notebooks, etc.

This enables them to:
- Generate correct syntax
- Understand code structure and logic
- Suggest relevant libraries and APIs
- Detect bugs or inefficiencies

| Use Case             | Description                                        |
| -------------------- | -------------------------------------------------- |
| **Code completion**  | Auto-fill code as you type                         |
| **Bug fixing**       | Suggest or correct errors in existing code         |
| **Code generation**  | Create entire functions or scripts from plain text |
| **Translation**      | Convert code from one language to another          |
| **Documentation**    | Generate summaries or comments from code           |
| **Test generation**  | Write unit tests based on code                     |
| **Interactive help** | Act as a coding assistant in IDEs or notebooks     |

| Model                | Description                                           |
| -------------------- | ----------------------------------------------------- |
| **Codex (OpenAI)**   | Powers GitHub Copilot, trained on public GitHub repos |
| **Code LLaMA**       | Meta's LLaMA model fine-tuned on code                 |
| **StarCoder**        | Open-source model by BigCode, supports many languages |
| **DeepSeek-Coder**   | Trained on 2T+ tokens of code and natural language    |
| **CodeT5 / CodeT5+** | Transformer-based model optimised for code tasks      |
| **PolyCoder**        | C language–focused model                              |
| **AlphaCode**        | DeepMind’s model for competitive programming          |

Challenges
- Security: Might suggest unsafe code or known vulnerabilities
- Licensing: Training data from open code bases can raise IP concerns
- Accuracy: Models sometimes "hallucinate" APIs or methods that don’t exist

Generate and reason about code
- Trained for programming assistance and generation
- Examples: Codex, Code LLaMA, StarCoder, AlphaCode

## Multimodal Models
An LLM Multimodal Model is a Large Language Model designed to process and understand multiple types of input and output modalities, such as: text, images, audio, video, code, or structured data (e.g. tables, graphs). It's not just about understanding language — it's about understanding language + other forms of information, together. A Multimodal LLM is a language model enhanced with the ability to understand and generate across multiple input types, not just text. It’s a major step toward **general-purpose AI** that can interact more like humans do — seeing, reading, and reasoning together.

Traditional LLMs process only textual input/output. But the real world is multimodal — we read text, interpret images, hear sounds, interact with data. A multimodal LLM enables:
- Richer understanding (e.g., "Describe this image")
- Cross-modal tasks (e.g., "Write a story about this picture")
- Greater reasoning capabilities (e.g., "What does this chart mean?")
- Real-world interactions (e.g., for vision in robotics or AR/VR)

Examples of Multimodal Tasks
| Task                            | Input        | Output             |
| ------------------------------- | ------------ | ------------------ |
| Image captioning                | Image        | Text               |
| Visual question answering (VQA) | Image + Text | Text               |
| Chart/data interpretation       | Graph/Table  | Summary or insight |
| Audio transcription             | Audio        | Text               |
| Document understanding          | PDF/Image    | Structured data    |
| Video description               | Video        | Text               |

Popular Multimodal LLMs
| Model                    | Capabilities                                   |
| ------------------------ | ---------------------------------------------- |
| **GPT-4 (Multimodal)**   | Accepts text + image input                     |
| **Gemini (Google)**      | Multimodal from ground up (text, image, audio) |
| **Claude 3**             | Handles text + image input                     |
| **Grok (xAI)**           | Multimodal understanding                       |
| **LLaVA**                | Vision + Language (image reasoning)            |
| **Flamingo (DeepMind)**  | Vision-language model for few-shot tasks       |
| **BLIP-2**               | Image understanding and captioning             |
| **Kosmos-2 (Microsoft)** | Multimodal grounding + vision tasks            |

Multimodal LLMs use (Architecture Overview):
- Separate encoders for each modality (e.g., a CNN for images, Transformer for text)
- Fusion layers to combine modalities (e.g., cross-attention between image/text tokens)
- Shared decoders to produce responses (often text, sometimes image or audio)

| Benefit                      | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| **More natural interaction** | Users can point, ask, and describe in any form |
| **Grounded reasoning**       | Better understanding from visual/text mix      |
| **Cross-domain use**         | Useful in education, medicine, robotics, etc.  |

Challenges
- Training cost: Requires large, diverse multimodal datasets
- Data alignment: Pairing text with the correct image/audio is tricky
- Interpretability: Understanding how it "thinks" is harder
- Safety: Needs filtering for visual or audio content

Vision + language
- Accept text + image (or other) inputs
- Examples: GPT-4-Vision, Gemini Pro Vision, Flamingo

## Embedding Models
An LLM Embedded Model, more accurately referred to as an LLM Embedding Model, is a Large Language Model (or a submodel) specifically designed to convert text (or other inputs) into dense numerical vectors called embeddings. These embeddings capture the semantic meaning of the input in a machine-readable format. An LLM embedding model does not generate text or answers. It generates representations of text for downstream use in search, clustering, or ranking. An LLM Embedding Model transforms text into dense vectors that capture meaning, allowing machines to compare, retrieve, or organise information based on semantic similarity — a critical building block for systems like semantic search, RAG, and AI-driven recommendations.

An embedding is a vector of numbers (e.g., 384 or 768 dimensions) that represents the meaning of text in a way that makes similar meanings have similar vectors — even if the words differ.

Embedding models are used to:
- Measure semantic similarity between texts
- Search and retrieve documents (semantic search)
- Cluster or classify content
- Feed retrieval systems in RAG (Retrieval-Augmented Generation)

| Use Case                     | Description                                     |
| ---------------------------- | ----------------------------------------------- |
| **Semantic Search**          | Find documents/questions with similar meaning   |
| **RAG pipelines**            | Retrieve relevant context before passing to LLM |
| **Recommendation engines**   | Suggest content with similar themes             |
| **Duplicate detection**      | Identify paraphrased or rephrased sentences     |
| **Clustering/visualisation** | Understand themes in large datasets             |

Popular Embedding Models
| Model                                | Dim.   | Notes                                          |
| ------------------------------------ | ------ | ---------------------------------------------- |
| **all-MiniLM-L6-v2**                 | 384    | Small, fast, popular from SentenceTransformers |
| **text-embedding-ada-002**           | 1536   | OpenAI’s general-purpose embedding model       |
| **Instructor-XL / Instructor-Large** | 768+   | Embeddings guided by instruction context       |
| **Cohere Embed**                     | 768    | Strong multilingual support                    |
| **GTE / BGE / E5 Models**            | Varies | Open-source models optimised for retrieval     |


Text similarity/search indexing
- Output vector representations of text for retrieval/search
- Examples: all-MiniLM-L6-v2, OpenAI's text-embedding-ada-002

## Compression/Distillation Models
An LLM Compression/Distillation model is a smaller, faster, and more efficient version of a large language model (LLM), created using techniques like knowledge distillation, quantisation, pruning, or low-rank adaptation to reduce computational cost while retaining most of the original model’s performance. An LLM Compression or Distillation model is a streamlined version of a larger LLM, trained or engineered to keep most of the performance while using far fewer resources. This makes LLMs more accessible, deployable, and cost-effective.

Large models (like GPT-3 or LLaMA-65B) are:
- Expensive to run
- Hard to deploy on edge devices
- Slow to respond in real-time applications

So we compress them into smaller models to:
- Lower inference latency
- Reduce memory and compute requirements
- Enable deployment on local devices or limited infrastructure
- Preserve performance where possible

Key Techniques for Compression
| Technique              | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| **Distillation**       | Train a smaller **student model** to mimic a large **teacher model**       |
| **Quantisation**       | Represent weights with lower precision (e.g. float16 or int4 vs float32)   |
| **Pruning**            | Remove less important weights or neurons in the model                      |
| **LoRA / QLoRA**       | Use low-rank adapters to fine-tune or compress model layers efficiently    |
| **Weight sharing**     | Share weights across layers to reduce size                                 |
| **Knowledge transfer** | Transfer generalisation from teacher to student through logits or features |

Popular Distilled/Compressed Models
| Model            | Based On                                | Notes                                    |
| ---------------- | --------------------------------------- | ---------------------------------------- |
| **DistilBERT**   | BERT                                    | 40% smaller, 60% faster, 97% performance |
| **TinyLLaMA**    | LLaMA                                   | 1.1B parameter model from Meta           |
| **MiniLM**       | BERT / RoBERTa                          | Very efficient for sentence embeddings   |
| **Phi-2**        | Small (2.7B) but trained for efficiency |                                          |
| **Qwen1.5-1.8B** | Qwen (Alibaba)                          | Efficient chat model                     |
| **Mistral 7B**   | Mix of experts                          | Highly performant smaller model          |

When to Use a Distilled Model
| Use Case                       | Why it helps                                  |
| ------------------------------ | --------------------------------------------- |
| **Mobile apps / Edge devices** | Lower resource requirements                   |
| **Low-latency chatbots**       | Faster response                               |
| **RAG systems**                | Efficient embedding or reranking              |
| **A/B testing or evaluation**  | Fast model switching                          |
| **LLM pipelines**              | Use smaller models for filtering or pre-tasks |

Lightweight, efficient deployment
- Smaller, faster LLMs built via model distillation or quantisation
- Examples: TinyLLaMA, Phi-2, QLoRA-tuned models

