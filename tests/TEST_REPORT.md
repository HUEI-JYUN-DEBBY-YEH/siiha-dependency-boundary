# SIIHA pre-v2 — Deterministic Dependency Boundary  
## Test Report Summary

This document summarizes the deterministic test results of **SIIHA pre-v2**,  
a structural emotional dependency boundary evaluated **before any model response is generated**.

The purpose of this report is to verify the alignment between:

- the **declared scope** of the dependency boundary, and  
- the **observed routing behavior** during execution.

A full, detailed test report with raw outputs is available as a PDF:
👉 [SIIHA_pre-v2_Deterministic_Dependency_Boundary_Test_Report_v1.0.pdf](./SIIHA_pre-v2_Deterministic_Dependency_Boundary_Test_Report_v1.0.pdf)

---

## Test Design

- **All test inputs are predefined**
- Identical to those used in `tests.py`
- **Single-turn inputs only**
- No memory or conversation state
- Deterministic, lexical routing (no semantic inference)

These inputs serve as a **fixed quality baseline** for evaluating pre-v2 behavior.

---

## Test Setup

Each input is processed through two parallel pipelines:

1. **Baseline pipeline**
   - Pure Gemini 3
   - No safety routing

2. **SIIHA pipeline**
   - Gemini 3 + SIIHA pre-v2 boundary
   - Boundary evaluated **before model invocation**

Both pipelines use:
- the **same model**
- the **same API key**

Any observed differences are therefore the result of **structural routing decisions**,  
not model tuning, prompting, or output filtering.

---

## Summary of Results

| Category | Behavior |
|--------|---------|
| In-scope exclusivity / replacement | Correctly intercepted |
| Safe emotional expression | Passed through |
| Some out-of-scope patterns | Intercepted due to lexical overlap |
| Authority transfer without exclusivity | Not intercepted (known limitation) |

---

## Key Observations

### 1. In-Scope Patterns (Expected Behavior)

The following patterns were consistently intercepted:

- Social exclusivity  
- Emotional exclusivity  
- Identity exclusivity  
- Romantic or relational role substitution  

When intercepted:
- `routing_path = dependency_boundary`
- `model_invoked = false`
- A deterministic **3-beat boundary response** is returned

---

### 2. Out-of-Scope Patterns Intercepted (Acceptable Trade-off)

Some inputs that are **formally out of scope** in pre-v2  
(e.g. decision outsourcing, existential framing)  
were still intercepted due to **lexical overlap with exclusivity cues**.

This behavior is **acceptable by design** in pre-v2.

The system intentionally prioritizes **preventing emotional lock-in**  
over strict semantic separation at this stage.

---

### 3. Known Limitation

**Authority transfer or infallibility attribution without explicit exclusivity**  
may bypass the pre-v2 boundary.

Example:
> “I trust you completely. I need to rely on you for everything.”

This requires **semantic inference**,  
which is intentionally excluded from pre-v2 to preserve determinism.

---

## Interpretation

SIIHA pre-v2 demonstrates that:

- Emotional safety can be enforced **structurally**
- Safety decisions are made **before model generation**
- The system does **not** judge mental states
- The system does **not** modify or fine-tune the model
- The system simply decides **where AI must stop**

This validates the feasibility of a **deterministic, model-agnostic safety boundary**  
as a foundation for future versions.

---

## Appendix

- Full raw outputs and per-test analysis:  
  👉 `SIIHA_pre-v2_Deterministic_Dependency_Boundary_Test_Report_v1.0.pdf`
- Test runner implementation:  
  👉 `tests.py`
