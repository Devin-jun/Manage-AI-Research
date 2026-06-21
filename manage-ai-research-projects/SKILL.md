---
name: manage-ai-research-projects
description: Manage AI-era computational research projects with reproducible directory structures, metadata, decisions, AI workflow records, results tracking, and manuscript-ready outputs. Use when creating a new scientific project, organizing an existing project, auditing reproducibility, or managing Claude Code/Codex-assisted research workflows.
---

# Manage AI Research Projects

## Operating Principles

Manage research projects around four outcomes: findable files, rerunnable analyses, traceable scientific claims, and easy manuscript or presentation delivery.

Use the simplified project template by default. Add optional folders only when the project actually needs them.

Keep raw data immutable. Never move, rewrite, delete, or rename raw data unless the user explicitly asks for that operation after seeing the plan.

Separate AI draft outputs from reviewed project assets. AI-generated code or interpretation starts in `ai_workflow/generated_code/` or `ai_workflow/reviewed_outputs/`; only move it into `code/`, `results/`, or `manuscript/` after human review.

## Choose the Workflow

1. For a new project, scaffold the simplified structure, then fill the entry files with the project goal, data sources, main analysis, owner, and current status.
2. For an existing project, inventory files first, identify data/code/results/manuscript/AI assets, then propose a migration plan before editing or moving files.
3. For a reproducibility audit, inspect structure, metadata, decisions, environment files, result traceability, naming, and AI workflow separation. Return a prioritized report.
4. For ongoing project maintenance, update `project.yaml`, `docs/decisions.md`, `ai_workflow/ai_notes.md`, and pointers to key results whenever the project direction or evidence changes.

## Default Project Structure

Use this core layout unless the user requests a smaller or larger template:

```text
PROJECT_NAME/
├── README.md
├── project.yaml
├── docs/
│   ├── project_brief.md
│   ├── decisions.md
│   ├── meeting_notes/
│   └── literature_notes/
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
├── configs/
├── code/
│   ├── notebooks/
│   ├── scripts/
│   ├── src/
│   └── workflows/
├── ai_workflow/
│   ├── prompts/
│   ├── agent_runs/
│   ├── generated_code/
│   ├── reviewed_outputs/
│   └── ai_notes.md
├── results/
│   ├── tables/
│   ├── figures/
│   ├── models/
│   ├── reports/
│   └── logs/
├── manuscript/
│   ├── figures/
│   ├── tables/
│   ├── drafts/
│   └── supplementary/
└── env/
```

Read `references/directory_template.md` when the task needs directory rationale, optional folders, or Git tracking rules.

## Scripted Operations

Use scripts for repeatable project setup and auditing. Resolve paths relative to this skill directory; in Claude Code, `${CLAUDE_SKILL_DIR}` points to it.

Create a new project:

```bash
python scripts/init_research_project.py PROJECT_NAME --root . --title "Project title" --owner "Owner name" --question "Main scientific question"
```

Audit an existing project:

```bash
python scripts/audit_research_project.py PROJECT_PATH
```

If the user wants manual edits instead of scripts, follow the same templates and checks.

## New Project Procedure

1. Infer or ask for the project name, scientific question, owner, and data type. If details are unavailable, create explicit placeholders.
2. Scaffold the default structure.
3. Fill `README.md` as a short project entry point, not a manuscript draft.
4. Fill `project.yaml` as a machine-readable project card.
5. Add an initial entry to `docs/decisions.md`.
6. Add `ai_workflow/ai_notes.md` with the AI usage boundary.
7. Add `.gitignore` rules that keep large raw data, checkpoints, temporary logs, and bulky processed artifacts out of Git.

## Existing Project Procedure

1. Inventory files with fast filesystem tools.
2. Classify each file group as data, metadata, code, config, AI workflow, result, manuscript, environment, reference, or archive candidate.
3. Identify risks before changing anything: raw data mixed with processed data, final results without generating code, AI drafts mixed into formal outputs, missing metadata, or unclear versions.
4. Present a migration plan with exact source and destination paths.
5. Only move or edit files after the user approves the plan if the changes affect existing data or irreversible structure.
6. After migration, create or update entry files and run the audit script.

## Audit Procedure

Check these points and report missing items by priority:

- Project entry: `README.md`, `project.yaml`, owner, status, scientific question.
- Data integrity: raw data isolated, metadata present, processed data separated.
- Reproducibility: scripts/workflows, configs, environment files, logs, and result-generation path.
- Traceability: important figures/tables link back to data, code, parameters, and decisions.
- AI workflow: prompts, generated code, agent runs, reviewed outputs, and AI usage notes are separated.
- Delivery: manuscript figures/tables/drafts are distinct from exploratory results.
- Naming: files use dates, object/action labels, and versions; vague names like `final.xlsx` are flagged.

Read `references/file_naming.md` for detailed naming rules. Read `references/ai_workflow_rules.md` for AI usage, review, and agent-run trace expectations.
