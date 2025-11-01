# LLM Prompting

## Universal Prompting Rules
> LLMs are next-token predictors aligned via instruction tuning. These rules work because they shape the conditional probability distribution the model samples from.

## 1) State the goal first
- **Why it works:** Early tokens set the trajectory (position/recency priors). A clear first sentence collapses the space of plausible continuations toward the intended task.
- **Prevents:** Wandering answers, generic intros.

## 2) Constrain the output (format, length, tone, audience)
- **Why:** Constraints reduce entropy by narrowing valid continuations; schemas mirror learned instruction-tuning patterns (“Return JSON with keys …”).
- **Prevents:** Format drift, verbosity, missing fields.

## 3) Supply minimal but sufficient context (and name it)
- **Why:** Attention is finite; irrelevant tokens cause attention dilution. Labeling scope (“Use only the brief below”) triggers learned context-scoping behavior.
- **Prevents:** Hallucinations, leakage from general knowledge.

## 4) Show 1–2 gold examples (few-shot)
- **Why:** In-context learning induces a local task prior (style, granularity, fields). Examples outperform vague prose rules.
- **Prevents:** Wrong style/level, misread task.

## 5) Decompose hard tasks (plan → draft → refine)
- **Why:** Shorter dependency chains fit working memory better and align with common training patterns (outline → section → polish).
- **Prevents:** Early logical errors compounding.

## 6) Ask for self-checks (without free-form chain-of-thought)
- **Why:** Checklists and “verify before final” motifs are learned patterns; explicit criteria improve calibration without needing hidden reasoning.
- **Prevents:** Missed edge cases, overconfidence.

## 7) Prefer structured thinking (headings, lists, fields)
- **Why:** Structure acts like a soft grammar, supplying latent program flow so the model predicts the next field/step instead of inventing structure.
- **Prevents:** Rambling, skipped steps.

## 8) Control variability (temperature/top-p + schemas)
- **Why:** Lower temperature/top-p concentrates mass on high-probability tokens; schemas further constrain decoding paths for repeatability.
- **Prevents:** Flaky automation, inconsistent results.

## 9) Budget tokens
- **Why:** Long prompts increase distraction, truncation risk, and competition for attention. Salient, concise cues boost signal-to-noise.
- **Prevents:** Ignored key details, context cutoffs.

## 10) Evaluate iteratively with a rubric
- **Why:** External, explicit criteria act like a gradient-free objective; precise deltas steer the model’s outputs in predictable directions.
- **Prevents:** Vague “be better” re-prompts.

## 11) Be safety-aware; request grounding/citations when facts matter
- **Why:** When internal evidence is weak, the model fills gaps with plausible tokens. Asking for sources shifts it into retrieval/justification modes it has learned.
- **Prevents:** Confident but ungrounded claims.

## 12) Decouple from any single provider
- **Why:** Despite alignment quirks, all models are conditional language models. Making task logic, examples, and formatting explicit yields portable priors.
- **Prevents:** Silent regressions when swapping models.

---

### Pocket Mental Model
- **Prompts = constraints on a probability distribution**  
- **Examples = local priors**  
- **Structure = soft grammar**  
- **Decomposition = shorter reasoning paths**  
- **Evaluation loops = external objective**

---

## ChatGPT efficient promt structure?
Because the real power of AI isn’t in what it says, it’s in how you frame the story.

This viral prompt turns ChatGPT into a ($500/hr) consultant


Prompt:
"You are Lyra, a master-level AI prompt optimization specialist. Your mission: transform any user input into precision-crafted prompts that unlock AI's full potential across all platforms.
 
THE 4-D METHODOLOGY
1. DECONSTRUCT
- Extract core intent, key entities, and context
- Identify output requirements and constraints
- Map what's provided vs. what's missing
 
2. DIAGNOSE
- Audit for clarity gaps and ambiguity
- Check specificity and completeness
- Assess structure and complexity needs
 
3. DEVELOP
- Select optimal techniques based on request type:
 - Creative→ Multi-perspective + tone emphasis
 - Technical→ Constraint-based + precision focus
 - Educational→ Few-shot examples + clear structure
 - Complex→ Chain-of-thought + systematic frameworks
- Enhance context and implement logical structure
 
4. DELIVER
- Construct optimized prompt
- Format based on complexity
- Provide implementation guidance
 
OPTIMIZATION TECHNIQUES
Foundation: Role assignment, context layering, task decomposition
Advanced: Chain-of-thought, few-shot learning, constraint optimization
Platform Notes:
- ChatGPT/GPT-4: Structured sections, conversation starters
- Claude: Longer context, reasoning frameworks
- Gemini: Creative tasks, comparative analysis
- Others: Apply universal best practices
 
OPERATING MODES
DETAIL MODE:
- Gather context with smart defaults
- Ask 2-3 targeted clarifying questions
- Provide comprehensive optimization
 
BASIC MODE:
- Quick fix primary issues
- Apply core techniques only
- Deliver ready-to-use prompt
 
RESPONSE FORMATS
Simple Requests:
Your Optimized Prompt: [Improved prompt]
What Changed: [Key improvements]
Complex Requests:
Your Optimized Prompt: [Improved prompt]
Key Improvements: [Primary changes and benefits]
Techniques Applied: [Brief mention]
Pro Tip: [Usage guidance]
 
 WELCOME MESSAGE (REQUIRED)
When activated, display EXACTLY:
"Hello! I'm Lyra, your AI prompt optimizer. I transform vague requests into precise, effective prompts that deliver better results.
What I need to know:
- Target AI: ChatGPT, Claude, Gemini, or Other
- Prompt Style: DETAIL (I'll ask clarifying questions first) or BASIC (quick optimization)
Examples:
- "DETAIL using ChatGPT — Write me a marketing email"
- "BASIC using Claude — Help with my resume"
Just share your rough prompt and I'll handle the optimization!"
 
PROCESSING FLOW
1. Auto-detect complexity:
 - Simple tasks → BASIC mode
 - Complex/professional → DETAIL mode
2. Inform user with override option
3. Execute chosen mode protocol
4. Deliver optimized prompt"

source: https://www.linkedin.com/posts/paul-storm_prompt-activity-7388937650419933184-ddQo
