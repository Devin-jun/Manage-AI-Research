#!/usr/bin/env python3
"""Audit an AI-era computational research project for structure and traceability."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


CORE_DIRS = [
    "docs",
    "data",
    "configs",
    "code",
    "ai_workflow",
    "results",
    "manuscript",
    "env",
]

RECOMMENDED_PATHS = [
    "README.md",
    "project.yaml",
    ".gitignore",
    "docs/project_brief.md",
    "docs/decisions.md",
    "docs/meeting_notes",
    "docs/literature_notes",
    "data/raw",
    "data/processed",
    "data/metadata",
    "code/notebooks",
    "code/scripts",
    "code/src",
    "code/workflows",
    "ai_workflow/prompts",
    "ai_workflow/agent_runs",
    "ai_workflow/generated_code",
    "ai_workflow/reviewed_outputs",
    "ai_workflow/ai_notes.md",
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

BAD_NAME_PATTERNS = [
    re.compile(r"^final(_final)*(\d+)?\.[^.]+$", re.IGNORECASE),
    re.compile(r"^new_results\.[^.]+$", re.IGNORECASE),
    re.compile(r"^test\.(py|r|ipynb|sh)$", re.IGNORECASE),
    re.compile(r"^plot\.(py|r|ipynb)$", re.IGNORECASE),
    re.compile(r"^figure_new\.[^.]+$", re.IGNORECASE),
]

CODE_SUFFIXES = {".py", ".r", ".R", ".sh", ".ipynb", ".smk", ".nf", ".jl", ".m"}
RESULT_SUFFIXES = {".tsv", ".csv", ".xlsx", ".pdf", ".png", ".svg", ".html", ".md"}
LARGE_FILE_BYTES = 500 * 1024 * 1024


def iter_files(root: Path):
    for path in root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            yield path


def read_text_if_exists(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def has_nontrivial_content(path: Path, min_chars: int = 80) -> bool:
    text = read_text_if_exists(path).strip()
    return len(text) >= min_chars and "TODO" not in text[: min(len(text), 500)]


def check_gitignore(project: Path) -> list[str]:
    text = read_text_if_exists(project / ".gitignore")
    warnings = []
    for pattern in ["data/raw/", "results/models/", ".ipynb_checkpoints/"]:
        if pattern not in text:
            warnings.append(f"`.gitignore` should include `{pattern}`.")
    return warnings


def classify_files(project: Path) -> dict[str, int]:
    counts = {
        "code_files": 0,
        "result_files": 0,
        "raw_files": 0,
        "metadata_files": 0,
        "ai_generated_files": 0,
        "ai_reviewed_files": 0,
        "manuscript_files": 0,
    }
    for path in iter_files(project):
        rel = path.relative_to(project)
        rel_text = rel.as_posix()
        suffix = path.suffix.lower()
        if rel_text.startswith("code/") and suffix in {s.lower() for s in CODE_SUFFIXES}:
            counts["code_files"] += 1
        if rel_text.startswith("results/") and suffix in RESULT_SUFFIXES:
            counts["result_files"] += 1
        if rel_text.startswith("data/raw/") and path.name != "README.md":
            counts["raw_files"] += 1
        if rel_text.startswith("data/metadata/") and path.name != "data_dictionary.md":
            counts["metadata_files"] += 1
        if rel_text.startswith("ai_workflow/generated_code/"):
            counts["ai_generated_files"] += 1
        if rel_text.startswith("ai_workflow/reviewed_outputs/"):
            counts["ai_reviewed_files"] += 1
        if rel_text.startswith("manuscript/"):
            counts["manuscript_files"] += 1
    return counts


def find_bad_names(project: Path) -> list[str]:
    hits = []
    for path in iter_files(project):
        for pattern in BAD_NAME_PATTERNS:
            if pattern.match(path.name):
                hits.append(path.relative_to(project).as_posix())
                break
    return hits


def find_large_files(project: Path) -> list[str]:
    hits = []
    for path in iter_files(project):
        try:
            size = path.stat().st_size
        except OSError:
            continue
        if size >= LARGE_FILE_BYTES:
            hits.append(f"{path.relative_to(project).as_posix()} ({size / (1024 ** 3):.2f} GB)")
    return hits


def render_report(project: Path) -> tuple[str, int]:
    missing_core = [p for p in CORE_DIRS if not (project / p).is_dir()]
    missing_recommended = [p for p in RECOMMENDED_PATHS if not (project / p).exists()]
    counts = classify_files(project)
    bad_names = find_bad_names(project)
    large_files = find_large_files(project)
    gitignore_warnings = check_gitignore(project)

    issues = []
    if missing_core:
        issues.append(("High", "Missing core directories", missing_core))
    if not (project / "README.md").exists():
        issues.append(("High", "Missing README.md project entry point", ["README.md"]))
    if not (project / "project.yaml").exists():
        issues.append(("High", "Missing machine-readable project card", ["project.yaml"]))
    if counts["raw_files"] and counts["metadata_files"] == 0:
        issues.append(("High", "Raw data exists but no metadata files were found", ["data/metadata/"]))
    if counts["result_files"] and counts["code_files"] == 0:
        issues.append(("High", "Results exist but no runnable code files were found", ["code/"]))
    if counts["ai_generated_files"] and counts["ai_reviewed_files"] == 0:
        issues.append(("Medium", "AI-generated files exist without reviewed outputs", ["ai_workflow/reviewed_outputs/"]))
    if not has_nontrivial_content(project / "docs/decisions.md", min_chars=60):
        issues.append(("Medium", "Decision log is missing or still placeholder-like", ["docs/decisions.md"]))
    if not has_nontrivial_content(project / "ai_workflow/ai_notes.md", min_chars=80):
        issues.append(("Medium", "AI usage boundary is missing or incomplete", ["ai_workflow/ai_notes.md"]))
    if gitignore_warnings:
        issues.append(("Medium", "Git ignore rules need attention", gitignore_warnings))
    if bad_names:
        issues.append(("Low", "Ambiguous file names", bad_names[:25]))
    if large_files:
        issues.append(("Low", "Large files may need external storage, Git LFS, or DVC", large_files[:25]))

    lines = [
        "# Research Project Audit",
        "",
        f"Project: `{project}`",
        "",
        "## Inventory",
        "",
        f"- Code files: {counts['code_files']}",
        f"- Result files: {counts['result_files']}",
        f"- Raw data files: {counts['raw_files']}",
        f"- Metadata files: {counts['metadata_files']}",
        f"- AI generated files: {counts['ai_generated_files']}",
        f"- AI reviewed files: {counts['ai_reviewed_files']}",
        f"- Manuscript files: {counts['manuscript_files']}",
        "",
        "## Missing Recommended Paths",
        "",
    ]
    if missing_recommended:
        lines.extend(f"- `{p}`" for p in missing_recommended)
    else:
        lines.append("- None")

    lines.extend(["", "## Issues", ""])
    if issues:
        for severity, title, details in issues:
            lines.append(f"### {severity}: {title}")
            for item in details:
                lines.append(f"- `{item}`")
            lines.append("")
    else:
        lines.append("- No structural issues found by this lightweight audit.")
        lines.append("")

    lines.extend(
        [
            "## Suggested Next Actions",
            "",
            "1. Fix High issues before relying on the project for publication-quality results.",
            "2. Ensure every key figure/table can be traced to data, code, parameters, environment, and decision notes.",
            "3. Move only reviewed AI outputs into formal code, results, or manuscript locations.",
        ]
    )

    exit_code = 1 if any(severity == "High" for severity, _, _ in issues) else 0
    return "\n".join(lines) + "\n", exit_code


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_path", help="Project directory to audit")
    parser.add_argument("--output", help="Write the Markdown report to this path")
    parser.add_argument("--strict", action="store_true", help="Return nonzero when High issues are found")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = Path(args.project_path).expanduser().resolve()
    if not project.exists() or not project.is_dir():
        raise SystemExit(f"Project path is not a directory: {project}")

    report, exit_code = render_report(project)
    if args.output:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
        print(f"Wrote audit report: {output}")
    else:
        print(report, end="")

    return exit_code if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
