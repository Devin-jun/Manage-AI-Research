# Manage AI Research Projects

`manage-ai-research-projects` is an Agent Skill for organizing AI-era computational research projects. It helps Claude Code, Codex, and other skills-compatible agents create reproducible project structures, audit existing projects, separate AI-generated drafts from reviewed outputs, and keep scientific results traceable to data, code, parameters, environment, decisions, and manuscript deliverables.

The skill is based on a lightweight research project management template for computational biology, bioinformatics, AI-assisted scientific workflows, RAG/agentic screening projects, model benchmarks, and manuscript-oriented analysis projects.

## Repository Layout

```text
.
└── manage-ai-research-projects/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/
```

The installable skill package is the `manage-ai-research-projects/` directory.

## Install

### Claude Code

Install as a personal skill:

```bash
mkdir -p ~/.claude/skills
cp -R manage-ai-research-projects ~/.claude/skills/
```

Or install into one project:

```bash
mkdir -p .claude/skills
cp -R manage-ai-research-projects .claude/skills/
```

Invoke it directly in Claude Code with:

```text
/manage-ai-research-projects
```

### Codex

Install as a personal Codex skill:

```bash
mkdir -p ~/.codex/skills
cp -R manage-ai-research-projects ~/.codex/skills/
```

Then ask Codex to use `$manage-ai-research-projects`.

## Use From GitHub

Users can download the repository ZIP or clone it, then copy the `manage-ai-research-projects/` directory into their agent's skills directory.

Example:

```bash
git clone https://github.com/Devin-jun/Manage-AI-Research.git
cp -R Manage-AI-Research/manage-ai-research-projects ~/.claude/skills/
```

## Capabilities

- Create a simplified research project skeleton with `README.md`, `project.yaml`, data/code/results/manuscript folders, and AI workflow records.
- Audit an existing project for missing metadata, weak reproducibility, unclear result traceability, ambiguous file names, and mixed AI draft/final outputs.
- Preserve raw data as immutable and separate it from processed analysis-ready files.
- Keep AI-generated code, prompts, agent traces, and reviewed outputs in distinct locations.
- Support manuscript and presentation delivery by keeping final assets separate from exploratory analysis results.

## Validate Locally

Run the setup script on a temporary project:

```bash
python3 manage-ai-research-projects/scripts/init_research_project.py demo_project --root /tmp --title "Demo Project"
```

Audit the generated project:

```bash
python3 manage-ai-research-projects/scripts/audit_research_project.py /tmp/demo_project
```

Check Python syntax:

```bash
PYTHONPYCACHEPREFIX=/tmp/skill_pycache python3 -m py_compile \
  manage-ai-research-projects/scripts/init_research_project.py \
  manage-ai-research-projects/scripts/audit_research_project.py
```

## Publishing Notes

For skill registries or hubs, point to the installable skill directory:

```text
manage-ai-research-projects/
```

The skill follows the Agent Skills directory convention:

```text
skill-name/
├── SKILL.md
├── scripts/
└── references/
```

`agents/openai.yaml` is optional Codex-facing metadata and does not affect Claude Code compatibility.

## License

MIT License. See [LICENSE](LICENSE).
