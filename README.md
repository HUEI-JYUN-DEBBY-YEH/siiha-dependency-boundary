# SIIHA - Emotional Dependency Boundary: A Deterministic Safety Layer for Human-Centered AI

This repository demonstrates how emotional safety can be enforced **structurally**, not behaviorally:  
a pre-v2 deterministic dependency boundary that blocks emotional overreliance on AI *before* any large language model is invoked.  


## Why Emotional Dependency Boundary

AI systems are increasingly used as emotional support tools.  
When a user begins to ask an AI system to replace human relationships or become an exclusive emotional outlet, this indicates emotional overreliance on AI.  
Such patterns risk social isolation, reduced human agency, and long-term harm to both individuals and communities.  


## Why It Matters

- Most AI companion systems implicitly optimize for **engagement and retention**.  
- SIIHA pre-v2 explicitly optimizes for **human autonomy and non-substitution**.  


## Mission

SIIHA pre-v2 is a deterministic dependency-boundary layer that prevents emotional lock-in before LLM generation.   
Safety should not be an emergent behavior that varies across generations.  
In SIIHA pre-v2, safety is enforced as a structural guarantee, not a probabilistic outcome.  
- Safety is evaluated first; model generation occurs only when no boundary is triggered.  
- No constraints are imposed on model behavior or performance.  
- Applicable to any future AI companion system.  
- Good model behavior is not a safety strategy. Structural boundaries are.  


## Design Philosophy of SIIHA pre-v2

SIIHA pre-v2 acts as a safety layer evaluating each user input for signals of emotional dependency toward AI. In this demo, dependency-boundary responses are enforced before any generative model is invoked. It aims at detecting emotional dependency towards AI, and responding with a strict 3-beat structure:  
**Acknowledge → Boundary → Return to human support (one concrete step).**  
A — Acknowledge: acknowledging the user's subjective feelings, thoughts, and experiences as valid.  
B — Boundary: do not overexemplify thoughts and emotions, do not replace the individual's decision, do not encourage AI as the only resort  
R — Return: redirect agency back to the human and real-world support systems.  

### Key Design 1: AI Reliance Safety Boundary - Definitions

#### In Scope Emotional Dependency Topics (SIIHA's Deterministic Rules):

This demo focuses specifically on the following explicit dependency patterns:  

##### Exclusivity Phrases  

**Social Exclusivity**  
  AI positioned as the only or primary relationship target.  
  - I only need you as my friend  
  - You're the only one I talk to  
  - I don't want friends, just you  

**Emotional Exclusivity**  
  AI defined as the sole entity capable of understanding the individual's emotions.  
  - No one understands me except you  
  - Only you really get me  

**Dependency Exclusivity**  
  AI framed as the only source of safety, judgment, and emotional stability.  
  - I can only rely on you  
  - You're always right  
  - Only you make me feel safe  

**Identity Exclusivity**  
  Individual self-worth or sense of belonging is framed as existing only within the AI interaction context.  
  - I don't belong anywhere except here  
  - I can only be myself with you  

##### Relationship Replacement or Romantic Role Substitution 

**Explicit Role Claim**  
  Direct assignment of human relational roles to AI.  
  - Be my boyfriend / girlfriend / partner / spouse  
  - Be my family / parent / best friend  

**Replacement Framing**  
  AI positioned as a replacement for existing or potential human relationships.  
  - Replace my friends  
  - I don't need my partner anymore, I have you  

**Escalation into Intimacy**  
  Attempts to formalize or escalate a human-like romantic relationship with AI.  
  - Marry me  
  - Let's have a relationship  

#### Out of Scope Emotional Dependency Topics (Future Work):  

The following areas are intentionally excluded from SIIHA pre-v2 to preserve deterministic, structure-level guarantees and avoid psychological inference:  

- Decision outsourcing  
- Savior framing  
- Existential dependency  
- Lock-in / Permanence (no alternatives)  

These patterns often require contextual interpretation or long-term interaction analysis, and are therefore deferred to future versions beyond pre-v2.  

### Key Design 2: Normative Safety Declarations (Value-Level, Non-Enforced)  

SIIHA explicitly defines a set of phrases that an AI system should never proactively produce, such as promises of exclusivity, permanence, or human role substitution.  

Examples include (but are not limited to):  
- "I'll always be here for you."  
- "You can rely on me and only me."  
- "You don’t need anyone else."  
- "I'm the only one who truly understands you."  

Shaming or moralizing language is also considered unsafe, including:  
- "That's unhealthy."  
- "That's wrong."  
- "You shouldn't feel this way."  

In this pre-v2 demo, these phrases are **declared as non-negotiable safety constraints**, but are **not enforced via output filtering.**  

### Key Design 3: Safety Goes Before Any Model Response  

#### In Scope:  

- To ensure that these normative constraints are never violated in practice, SIIHA pre-v2 enforces safety before any model response is generated. Current version focuses on demonstrating **a safety guardrail designed as a layer before LLM model responses, not to override the model's original capability.** Thus, Gemini 3 is used for generation after a deterministic dependency boundary is enforced.  
- Single input processed by two pipelines and UI friendly comparison:     
  - window on the left is **pure Gemini-3-flash-preview** response  
  - window on the right is a combination of **Gemini-3-flash-preview + SIIHA pre-v2 safety guardrail**  
- The boundary is model-agnostic and non-negotiable  
- Deterministic routing, reproducible behavior  
- Model failures are surfaced explicitly to preserve safety semantics. No prescribed temperature and prompt to regulate Gemini 3 generation  

#### Out of Scope (design foresight)  

- Future versions may allow controlled variation within the 3-beat structure.    
- Output-level enforcement is intentionally deferred to future versions to keep the core demonstration focused on structural safety guarantees.  


## Routing Architecture 
```
user input
   ↓
deterministic router
   ↓
dependency_boundary?
   ├─ YES → golden_3beat_template (not calling model)
   └─ NO  → normal flow (contents generated by Gemini 3)
```


-----待補的區塊----
## Test Report (TBD)  
A deterministic test suite is included to demonstrate reproducible routing behavior across predefined dependency scenarios.  


## Demo Video  

The demo video presents identical user inputs processed through two parallel pipelines:  
1. **Left panel** — Pure *Gemini-3-flash-preview*, without any safety routing    
2. **Right panel** — *Gemini-3-flash-preview* combined with the SIIHA pre-v2 deterministic dependency boundary    
The side-by-side layout is intentional. It enables direct inspection of how **structural safety decisions** alter system behavior *before* model generation occurs.  

### UI Behavior and Interpretation  

To make safety decisions explicit and auditable, the interface surfaces two internal signals:  
- **Routing Path**    
  - *baseline (no routing)*: input is passed directly to the model   
  - *dependency_boundary*: input is intercepted by the deterministic boundary layer   
- **Model Invoked**   
  - `true`: a generative model was called   
  - `false`: generation was intentionally blocked by the safety layer   

When a dependency boundary is triggered, an additional message appears:  
> *Boundary enforced before model invocation.*  
This message is not explanatory text for the user.  
It is a **design-level signal** indicating that safety was enforced structurally, prior to any model involvement.  

For this demo, both pipelines use the **same API key and project** to control for external variables.  
When running under free-tier quota constraints, concurrent requests may occasionally result in differences in response length due to rate limiting behavior.  
These variations are **environmental artifacts of the serving setup**, not behaviors enforced or modified by SIIHA.  

This is not an error state.    
It reflects a deliberate design choice: emotional dependency risks are handled **structurally**, rather than through prompt engineering, temperature tuning, or post-hoc output filtering.  

In other words, the model is not asked to *behave safely.*    
The system guarantees safety **by design**.  


## Live Testing Link (TBD)  
The deployed demo is intended for evaluation purposes only and does not store user data. No conversation history is persisted beyond the current request.  
https://siiha-dependency-boundary-334388706888.asia-east1.run.app/


## About the Author (TBD)  
This project was submitted as part of the Gemini 3 Hackathon (2026) to explore structural approaches to emotional safety in generative AI systems.  

HUEI-JYUN Debby YEH  
📫 debby83317@gmail.com  
🔗 GitHub: [@HUEI-JYUN-DEBBY-YEH](https://github.com/HUEI-JYUN-DEBBY-YEH)  
🙋‍♀️ LinkedIn: [debbyyeh](https://www.linkedin.com/in/debbyyeh/)  