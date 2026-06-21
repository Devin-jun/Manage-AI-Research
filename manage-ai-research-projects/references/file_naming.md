# File Naming

Prefer names that stay useful months later.

## General Patterns

Use one of these patterns:

```text
YYYY-MM-DD_object_action_version.ext
project_datatype_analysis_version.ext
NN_action_object.ext
```

Rules:

- Use lowercase English for code and data.
- Use underscores between words.
- Use dates as `YYYY-MM-DD`.
- Avoid spaces in code, data, and result filenames.
- Include a version when files may be revised manually.
- Keep manuscript and presentation filenames readable, but still include date or version.

## Examples

Data:

```text
sample_info_2026-06-07.tsv
ptm_sites_uniprot_raw_2026-06-07.tsv
ptm_sites_functional_processed_v1.tsv
protein_embeddings_pi_proteoformer_v1.parquet
```

Scripts:

```text
01_download_uniprot.py
02_build_annotation_table.py
03_run_main_analysis.py
04_evaluate_results.py
05_generate_figures.py
```

Notebooks:

```text
2026-06-07_01_data_overview.ipynb
2026-06-08_02_embedding_retrieval_exploration.ipynb
2026-06-09_03_case_study_visualization.ipynb
```

Figures and tables:

```text
fig1_project_overview_v1.pdf
fig2_model_performance_v2.pdf
extended_data_fig1_qc_metrics_v1.pdf
table1_dataset_summary_v1.xlsx
```

AI workflow files:

```text
2026-06-07_ptm_reasoning_prompt_v1.md
2026-06-07_agent_run001_summary.md
2026-06-08_literature_summary_checked.md
```

## Flag These Names

```text
final.xlsx
final_final.xlsx
new_results.csv
test.py
plot.py
figure_new.pdf
```

When an ambiguous name is found, rename it only after checking references from notebooks, scripts, workflows, manuscripts, and collaborators.
