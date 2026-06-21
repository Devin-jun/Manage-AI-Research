# AI Workflow Rules

AI-assisted work is part of the project record. Keep it separate, reviewable, and traceable.

## Output Levels

- `draft`: AI-generated and not yet checked. Store in `ai_workflow/generated_code/` or an agent run folder.
- `reviewed`: Human checked and suitable as project evidence or support. Store in `ai_workflow/reviewed_outputs/`.
- `final`: Ready for manuscript, presentation, release, or delivery. Store in `manuscript/`, `results/`, or stable `code/` only after review.

## Folder Roles

- `ai_workflow/prompts/`: Reusable prompts that are project assets. Version prompts when they affect repeated analyses.
- `ai_workflow/agent_runs/`: Inputs, outputs, tool traces, and run summaries for autonomous or semi-autonomous agents.
- `ai_workflow/generated_code/`: AI-generated code drafts that have not been reviewed or integrated.
- `ai_workflow/reviewed_outputs/`: Checked AI summaries, code reviews, result interpretations, and literature notes used to support decisions.
- `ai_workflow/ai_notes.md`: Boundary statement describing how AI is used and what requires human confirmation.

## Agent Run Minimum Record

Each important agent run should preserve:

```text
input.json or input.md
output.json or output.md
tool_calls.json or trace summary
run_summary.md
```

`run_summary.md` should state:

- what the agent attempted
- which inputs and tools were used
- what output was produced
- what evidence supports the output
- what a human checked
- whether anything entered formal code, results, or manuscript outputs

## Human Review Checklist

Require human review before treating AI output as project evidence when it affects:

- sample groups or metadata interpretation
- statistical tests
- filtering criteria
- figure or table meaning
- biological or clinical conclusions
- manuscript claims
- reviewer responses
- wet-lab validation descriptions

## Prompt Versioning

Version prompts that are reused for literature review, result interpretation, agent screening, code review, or figure captioning.

Use names like:

```text
2026-06-07_literature_summary_prompt_v1.md
2026-06-08_ptm_reasoning_prompt_v2.md
```
