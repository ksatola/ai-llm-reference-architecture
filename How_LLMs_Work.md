# How LLMs Actually Work

## 1) What they are
- An LLM is a **probability machine**: given previous tokens (pieces of text), it predicts the **next token**. Do that many times → paragraphs, code, etc.
- The core architecture is a **Transformer** with **self-attention**, letting it weigh which parts of the context matter for the next token.

## 2) How they learn (pretraining → alignment)
1. **Tokenize** text into subword tokens (e.g., “play”, “##ing”).  
2. **Pretrain** on huge corpora with the objective “predict the next token.” This teaches grammar, facts, styles.  
3. **Supervised fine-tuning (SFT):** prompt–response pairs teach instruction following.  
4. **Preference optimization (e.g., RLHF/DPO):** human comparisons tune the model to prefer helpful, harmless, honest answers.  
5. **Domain tuning (optional):** specialize on code, legal, medical, etc.

> Result: it still predicts next tokens, but now it’s **aligned** to be useful to instructions.

## 3) How they answer you (inference)
- You provide a **prompt** (system message + instructions + context).  
- The model computes attention over tokens and outputs a **distribution over the next token**.  
- A **decoding strategy** samples from that distribution:
  - **Greedy/beam** → deterministic, often bland.
  - **Temperature/top-p** → more diverse/creative, more variance.
- Repeat token by token until a stop condition.

## 4) Why prompting works
- Prompts act as **constraints and examples** that shape the next-token distribution.  
- **Structure, schemas, and few-shot examples** provide a local “task prior,” reducing ambiguity.  
- **Decomposition** (plan → solve → verify) shortens reasoning chains the model must maintain.

## 5) Getting context in (and beyond)
- **Context window:** the model reads only *N* tokens. Summaries and selective context help.  
- **RAG (retrieval-augmented generation):** fetch relevant documents and include them in the prompt to ground answers.  
- **Tool use / function calling:** the model is prompted to call external tools (search, code exec, calculators) and integrate results—still via next-token prediction.

## 6) Strengths vs. limits
**Strengths**
- Flexible: one model, many tasks via prompting.
- Strong pattern completion, style transfer, synthesis.

**Limits**
- **Hallucinations:** fluent but wrong if not grounded.  
- **Context limits:** may misweight or forget details (**attention dilution**).  
- **Non-determinism:** sampling varies outputs.  
- **No true “understanding”:** models correlations; provide grounding (RAG/tools) for reliability.  
- **Bias & safety:** reflects training data and alignment choices.

## 7) Mental model (sticky version)
- **LLMs = next-token predictors**  
- **Prompt = constraints + examples**  
- **Attention = what to look at now**  
- **Decoding = how adventurous to be**  
- **RAG/tools = bring in facts and actions**

