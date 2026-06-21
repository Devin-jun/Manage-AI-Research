#!/usr/bin/env python3
"""Create a lightweight AI-era computational research project skeleton."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from textwrap import dedent


CORE_DIRS = [
    "docs/meeting_notes",
    "docs/literature_notes",
    "data/raw",
    "data/processed",
    "data/metadata",
    "configs",
    "code/notebooks",
    "code/scripts",
    "code/src",
    "code/workflows",
    "ai_workflow/prompts",
    "ai_workflow/agent_runs",
    "ai_workflow/generated_code",
    "ai_workflow/reviewed_outputs",
    "results/tables",
    "results/figures",
    "results/models",
    "results/reports",
    "results/logs",
    "manuscript/figures",
    "manuscript/tables",
    "manuscript/drafts",
    "manuscript/supplementary",
    "env",
]


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_file(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return "kept"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "wrote"


def readme_template(project_id: str, title: str, question: str, owner: str) -> str:
    return dedent(
        f"""\
        # {title or project_id}

        ## 1. Project Goal
        {question or "TODO: State the scientific question this project answers."}

        ## 2. Data
        TODO: Describe data sources, samples, species, assays, batches, and metadata.

        ## 3. Main Analysis
        TODO: Describe the core analysis path and where runnable scripts or workflows live.

        ## 4. Key Results
        TODO: Link the most important result tables, figures, reports, or models.

        ## 5. Reproducibility
        TODO: Explain how to rerun the core analysis from configs, code, and environment files.

        ## 6. Contact / Owner
        {owner or "TODO: Add project owner and contributors."}
        """
    )


def project_yaml_template(project_id: str, title: str, question: str, owner: str, workflow: str) -> str:
    today = date.today().isoformat()
    return dedent(
        f"""\
        project:
          name: {yaml_quote(project_id)}
          title: {yaml_quote(title or project_id)}
          owner: {yaml_quote(owner or "TODO")}
          status: active
          start_date: {yaml_quote(today)}

        scientific_question:
          main: {yaml_quote(question or "TODO: State the main scientific question.")}
          sub_questions: []

        data:
          raw_sources: []
          sensitive_data: false
          metadata_files:
            - data/metadata/

        analysis:
          workflow_manager: {yaml_quote(workflow)}
          languages: []
          key_scripts:
            - code/scripts/
          key_outputs:
            - results/tables/
            - results/figures/

        ai_workflow:
          enabled: true
          uses:
            - literature_summary
            - code_generation
            - result_interpretation
            - agentic_screening
          review_required: true
        """
    )


def decisions_template() -> str:
    today = date.today().isoformat()
    return dedent(
        f"""\
        # Decisions

        ## {today}
        Decision: Initialized the project using the AI-era research project template.
        Reason: Keep data, code, results, manuscript deliverables, and AI workflow records traceable.
        Impact: Future results should link back to data sources, code, parameters, environment, and review notes.
        """
    )


def project_brief_template(title: str, question: str) -> str:
    return dedent(
        f"""\
        # Project Brief

        ## Working Title
        {title or "TODO"}

        ## Scientific Question
        {question or "TODO"}

        ## Hypothesis / Rationale
        TODO

        ## Data and Materials
        TODO

        ## Planned Analyses
        TODO

        ## Expected Deliverables
        TODO
        """
    )


def ai_notes_template() -> str:
    return dedent(
        """\
        # AI Usage Notes

        AI tools may be used for literature summaries, code drafts, debugging, result interpretation drafts, figure captions, manuscript polishing, and agentic screening.

        Human review is required before using AI-generated scientific claims, statistical interpretations, figure/table content, reviewer responses, or manuscript text as final project output.

        Store reusable prompts in `ai_workflow/prompts/`, unreviewed AI-generated code in `ai_workflow/generated_code/`, agent traces in `ai_workflow/agent_runs/`, and checked AI outputs in `ai_workflow/reviewed_outputs/`.
        """
    )


def raw_data_readme() -> str:
    return dedent(
        """\
        # Raw Data

        Store immutable raw data here, or document the external/server path if the data is too large for the project directory.

        Do not manually edit, overwrite, or rename raw data files. Generate cleaned or analysis-ready files under `data/processed/`.
        """
    )


def data_dictionary_template() -> str:
    return dedent(
        """\
        # Data Dictionary

        Document sample IDs, group labels, batches, species, tissue, time point, assay platform, file paths, and any controlled vocabularies used by the project.
        """
    )


def gitignore_template() -> str:
    return dedent(
        """\
        # data
        data/raw/
        data/processed/*.h5ad
        data/processed/*.parquet
        data/processed/*.h5

        # results
        results/models/
        results/logs/
        results/exploratory/

        # environment
        .env
        .venv/
        __pycache__/
        .ipynb_checkpoints/

        # large scientific files
        *.bam
        *.fastq
        *.fastq.gz
        *.fq
        *.fq.gz
        *.mzML
        *.raw
        *.h5
        *.h5ad
        *.pt
        *.pth
        *.ckpt
        *.faiss
        """
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_name", help="Project directory name or path")
    parser.add_argument("--root", default=".", help="Root directory in which to create the project")
    parser.add_argument("--title", default="", help="Human-readable project title")
    parser.add_argument("--owner", default="", help="Project owner or lead")
    parser.add_argument("--question", default="", help="Main scientific question")
    parser.add_argument("--workflow-manager", default="none", help="Workflow manager, e.g. snakemake, nextflow, make, none")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_arg = Path(args.project_name).expanduser()
    project_dir = project_arg if project_arg.is_absolute() else Path(args.root).expanduser() / project_arg
    project_dir = project_dir.resolve()
    project_id = project_dir.name

    project_dir.mkdir(parents=True, exist_ok=True)
    for rel_dir in CORE_DIRS:
        (project_dir / rel_dir).mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": readme_template(project_id, args.title, args.question, args.owner),
        "project.yaml": project_yaml_template(project_id, args.title, args.question, args.owner, args.workflow_manager),
        ".gitignore": gitignore_template(),
        "docs/project_brief.md": project_brief_template(args.title or project_id, args.question),
        "docs/decisions.md": decisions_template(),
        "ai_workflow/ai_notes.md": ai_notes_template(),
        "data/raw/README.md": raw_data_readme(),
        "data/metadata/data_dictionary.md": data_dictionary_template(),
    }

    statuses = []
    for rel_path, content in files.items():
        status = write_file(project_dir / rel_path, content, args.force)
        statuses.append((status, rel_path))

    print(f"Created research project skeleton: {project_dir}")
    print("Directories:")
    for rel_dir in CORE_DIRS:
        print(f"  ensured {rel_dir}/")
    print("Files:")
    for status, rel_path in statuses:
        print(f"  {status:5} {rel_path}")
    if not args.force:
        print("Existing files were kept. Re-run with --force to overwrite template files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
