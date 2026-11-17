# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

I learned that AI assistance to improve my SoulVibes music recommendation system by reviewing existing code, debugging errors, and developing a multi-step Python workflow.

**What task did you give the agent?**

I asked Claude AI to help improve my existing music recommendation system by reviewing the recommendation logic, identifying errors, improving validation, and creating a workflow that checks the system before displaying recommendations.

**Prompts used:**

Explain errors and suggest fixes.
Review my existing music recommendation code and identify problems.
Help improve the recommendation scoring system.
Check whether the recommendation functions work correctly.

**What did the agent generate or change?**

With AI assistance, I developed src/agent.py to coordinate a multi-step Python workflow.

1. Validate the song dataset.
2. Validate user preferences.
3. Generate song recommendations.
4. Validate recommendation results.
5. Save an execution trace to logs/agent_trace.md.

I also created src/evaluate.py to test three user preference profiles and report pass/fail results.

**What did you verify or fix manually?**

I reviewed the generated code, corrected errors doing implementation, and tested the recommendation workflow by running:
python –m src.main

I also ran Python –m pytest, which passed all six automated tests, and python –m src.evaluate, which passed all three evaluation tests. I checked that the agent execution trace was created.

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

Not attempted. I focused on implementing the multi-step Python agent workflow, recommended validation, and evaluation script. I did not intentionally implement a specific software design pattern.

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->

Accepted AI suggestion:
I accepted the suggestion to create a multi-step workflow in src/agent.py. This improved my system by adding dataset validation, preference validation, recommendation validation, and execution logging.

Revise AI Suggestion:
I revised the description of the workflow, so it would not be presented as a fully autonomous AI agent. The final implementation uses predefined Python steps and existing validation functions rather than an autonomous large language model.

What I Learned and Limitations:
I learned that AI can help with debugging, code improvements, and developing new features. However, AI-generated code must be reviewed and tested before being used. One limitation is that the workflow follows predefined steps and does not independently make complex decisions. The evaluation script also checks basic recommendation validity rather than fully measuring recommendation relevance or user satisfaction.
