# Directory Template

Use this simplified template for AI-assisted computational research projects unless a project clearly needs more detail.

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

## Directory Roles

- `README.md`: Short human entry point. Explain the project goal, data, main analysis, key results, reproducibility path, and owner.
- `project.yaml`: Machine-readable project card for agents and scripts. Include project name, status, owner, scientific question, data sources, analysis workflow, and AI usage.
- `docs/`: Project thinking, meetings, literature notes, experiment notes, and decisions. Do not store final manuscript assets here.
- `data/raw/`: Immutable raw data or pointers to external/server raw data. Do not edit in place.
- `data/processed/`: Stable analysis-ready data generated from raw data or metadata.
- `data/metadata/`: Sample information, grouping, batch, clinical, species, tissue, time point, assay platform, and data dictionary files.
- `configs/`: Parameters, paths, sample sheets, and workflow configuration. Avoid hardcoding parameters in notebooks.
- `code/notebooks/`: Exploration. Stable logic should migrate to `code/scripts/`, `code/src/`, or `code/workflows/`.
- `code/scripts/`: Runnable scripts for data preparation, main analysis, evaluation, and figure generation.
- `code/src/`: Reusable modules.
- `code/workflows/`: Snakemake, Nextflow, Makefile, shell pipelines, or other orchestration.
- `ai_workflow/`: AI prompts, conversations, generated code, agent runs, reviewed AI outputs, and AI usage boundaries.
- `results/`: Analysis outputs. These are not necessarily manuscript-ready.
- `manuscript/`: Final or near-final delivery materials for papers, reports, talks, supplements, and responses.
- `env/`: `environment.yml`, `requirements.txt`, `Dockerfile`, lockfiles, and session information.

## Optional Additions

Add these only when needed:

- `data/external/`: Third-party databases or public downloads distinct from project raw data.
- `data/interim/`: Temporary intermediate files when a workflow produces many unstable transition products.
- `references/`: Local copies or links for protocols, key papers, database documentation, and external resources.
- `archive/`: Deprecated code, old results, or unused materials that are not active but should not be deleted yet.
- `code/tests/`: Add when shared code affects sample matching, coordinate transforms, filtering, statistics, model evaluation, or publication figures.

## Git Policy

Track:

- `README.md`
- `project.yaml`
- `docs/`
- `configs/`
- `code/`
- `ai_workflow/prompts/`
- `ai_workflow/reviewed_outputs/`
- `ai_workflow/ai_notes.md`
- `env/`
- `manuscript/drafts/`

Do not track by default:

- `data/raw/`
- large processed matrices or embeddings
- `results/models/`
- bulky logs
- checkpoints
- temporary notebooks checkpoints

Use Git LFS, DVC, object storage, or server path documentation for large files that must be versioned.
