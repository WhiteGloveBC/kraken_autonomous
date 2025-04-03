# ASZA — Lessons Learned (Kraken Autonomous Build)

---

## 1. Complexity Must Be Deferred

- Premature integration of Postgres, Redis, and LLM routers caused friction.
- The successful pivot was to begin with zero external services.
- Flat files, single purpose modules, and CLI-only tools allowed rapid testing.

---

## 2. GPT Needs a Reliable Context System

- LLMs forget context unless enforced via memory or structured prompt generation.
- Reflection, context files, and markdown history became critical.
- ASZA enforces structure that keeps agents focused and grounded.

---

## 3. Placeholder Logic Wastes Time

- Placeholder code creates the illusion of progress but increases friction later.
- John Wick (JW) was rebuilt with **fully functional logic** from the start.
- Every module must ship with a clear, testable output or it is restructured.

---

## 4. Self-Repairing Systems Require Feedback Loops

- Reflection alone is not enough — it must **trigger behavior**.
- `wrap_execution` and `send_alert` enforce visibility and reaction.
- JW now escalates clone counts, creates fixes, and optimizes based on logs.

---

## 5. Modular Enforcement Reduces Refactors

- The template system (`template_header`, `wrapper`, `footer`) ensures consistency.
- Updating global behavior is now a **one-file change**.
- Every new module instantly complies with alerts, logging, and env behavior.

---

## 6. Pushover Integration Changed Everything

- Real-time feedback revealed system flaws quickly.
- Alerts made the system feel alive — and made issues visible immediately.
- A powerful trigger loop: **code → run → reflect → alert → optimize**

---

## 7. GPT is Architect, Not Worker

- GPT is used to **plan and structure modules**.
- Actual code generation is routed to secondary models.
- GPT-4 (and Command A) are strategic — not the front-line builder.

---

## 8. John Wick Is a Required Component

- Passive systems fail silently. JW is an aggressive, parallel-thinking engine.
- JW components handle:
  - Broken module repair
  - Strategy compounding
  - Cloning and escalation
- JW enables autonomous survival and progress.

---

## 9. Git + Scheduler Close the Loop

- Git automation ensures version control for every improvement.
- Scheduler runs JW + sync every 15 minutes.
- These complete the system — **build, reflect, alert, store, repeat.**

---

## 10. This Is Not a Script. It's a System.

- ASZA is a philosophy and an architecture, not just code.
- It brings modular development, agentic evolution, and infrastructure control into one loop.
