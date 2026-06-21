---
tags:
  - Agent
  - "#项目管理"
---


# **计算科研项目文件目录管理建议：面向生物信息学与 AI 工作流**

## **一、核心原则**

计算科研项目的目录管理，不应该追求“看起来很工程化”，而应该服务于四个目标：

1. **找得到**：几个月后自己仍然能快速知道每个文件是什么、从哪里来、用于什么分析。
2. **跑得通**：关键结果可以从原始数据或中间数据重新生成，而不是依赖手动操作。
3. **说得清**：每张图、每个表、每个结论都能对应到数据来源、代码、参数、环境和分析记录。
4. **交付方便**：论文图表、汇报 PPT、补充表、审稿回复、数据上传材料能够从项目目录中自然沉淀出来。

对于生命健康类科研项目，目录规范不能照搬纯模拟或纯软件项目。因为这类项目往往同时包含：

- 原始实验数据；
- 样本信息和临床/实验 metadata；
- 多轮探索性分析；
- 论文图表和补充材料；
- 与湿实验、导师、合作者之间的沟通记录；
- AI 辅助分析、代码生成、文献总结、Agent 运行日志等新型工作流产物。

所以，推荐采用一种“科研问题导向 + 可复现分析 + AI 工作流记录”的轻量目录结构。

---

## **二、推荐项目目录模板**

建议每个独立科研项目使用如下结构：

```text
PROJECT_NAME/
├── README.md
├── project.yaml
├── .gitignore
├── docs/
│   ├── project_brief.md
│   ├── meeting_notes/
│   ├── literature_notes/
│   ├── experiment_notes/
│   └── decisions.md
├── data/
│   ├── raw/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   └── metadata/
├── configs/
│   ├── samples.yaml
│   ├── parameters.yaml
│   └── paths.yaml
├── code/
│   ├── notebooks/
│   ├── scripts/
│   ├── src/
│   ├── workflows/
│   └── tests/
├── ai_workflow/
│   ├── prompts/
│   ├── conversations/
│   ├── agent_runs/
│   ├── generated_code/
│   ├── reviewed_outputs/
│   └── ai_notes.md
├── results/
│   ├── exploratory/
│   ├── tables/
│   ├── figures/
│   ├── models/
│   ├── reports/
│   └── logs/
├── manuscript/
│   ├── figures/
│   ├── tables/
│   ├── supplementary/
│   ├── drafts/
│   └── responses/
├── env/
│   ├── environment.yml
│   ├── requirements.txt
│   ├── Dockerfile
│   └── session_info/
├── references/
│   ├── papers/
│   ├── protocols/
│   └── resources.md
└── archive/
    ├── old_results/
    ├── deprecated_code/
    └── unused/
```

这个模板中，真正每天会高频使用的是：

```text
data/
code/
results/
docs/
ai_workflow/
manuscript/
```

其他目录主要用于增强复现性和交付能力。

---

## **三、各目录的用途说明**


### 1.`README.md`：项目入口

`README.md` 是项目的总说明，建议控制在一屏到两屏内，不要写成论文。

建议包含：

```markdown
# PROJECT_NAME

## 1. Project Goal
这个项目要回答什么科学问题？

## 2. Data
数据来源是什么？包括哪些样本、物种、组学类型、实验批次？

## 3. Main Analysis
核心分析流程是什么？

## 4. Key Results
目前最重要的结果文件在哪里？

## 5. Reproducibility
如何重新运行核心分析？

## 6. Contact / Owner
项目负责人和主要贡献者。
```

重点是：别人打开项目目录后，能在 3 分钟内知道这个项目在做什么。

---

### 2. `project.yaml`：机器可读的项目卡片

相比 README，`project.yaml` 更适合被脚本、Agent、工作流系统读取。

示例：

```yaml
project:
  name: PTM_RAG
  title: PTM reasoning-oriented knowledge base
  owner: Jun Zhu
  status: active
  start_date: 2026-06-01

scientific_question:
  main: "How can analogical evidence improve PTM functional reasoning?"
  sub_questions:
    - "Can cross-species conserved PTM sites provide functional clues?"
    - "Can UniProt annotations enrich PTM reasoning?"

data:
  raw_sources:
    - UniProt
    - PTM databases
    - Proteoformer embeddings
  sensitive_data: false

analysis:
  workflow_manager: snakemake
  language:
    - python
  key_outputs:
    - results/tables/
    - results/figures/

ai_workflow:
  enabled: true
  model_usage:
    - literature summary
    - code generation
    - result interpretation
    - agentic screening
```

这个文件的价值在于：未来你搭建 AI Agent 或自动化项目管理系统时，可以直接读取项目基本信息。

---

###  3. `docs/` ：项目思考、会议和决策

`docs/` 不是放最终论文的地方，而是放“项目推进过程中的思考”。

推荐结构：

```text
docs/
├── project_brief.md
├── meeting_notes/
│   ├── 2026-06-07_group_meeting.md
│   └── 2026-06-14_collaboration_discussion.md
├── literature_notes/
│   ├── 2026-06-07_ptm_reasoning_review.md
│   └── 2026-06-08_agentic_science.md
├── experiment_notes/
│   ├── 2026-06-09_embedding_index_test.md
│   └── 2026-06-10_uniprot_annotation_test.md
└── decisions.md
```

其中最重要的是 `decisions.md`。

建议记录关键决策：

```markdown
# Decisions

## 2026-06-07
Decision: 将知识库定位为 annotation enrichment layer，而不是重复做向量检索。
Reason: 避免与 PTM-MSA 工具重复，降低系统复杂度。
Impact: KB 只负责富化注释，不负责召回。
```

很多项目后期最痛苦的不是没有结果，而是不知道“当时为什么这么做”。`decisions.md` 可以解决这个问题。

---

###  4.`data/` ：数据分层管理

推荐结构：

```text
data/
├── raw/
├── external/
├── interim/
├── processed/
└── metadata/
```

#### **`data/raw/`**

放原始数据，原则是：

raw data 只读，不手动改，不覆盖。

例如：

```text
data/raw/
├── uniprot/
├── mass_spec/
├── sequencing/
└── public_database/
```

如果原始数据太大，不建议直接放 Git，而是在目录中放说明文件：

```text
data/raw/README.md
```

内容示例：

```markdown
# Raw Data

原始数据存储在服务器路径：

/data/project/PTM_RAG/raw/

不要手动修改 raw data。
如果需要清洗，请在 data/interim/ 或 data/processed/ 中生成新文件。
```

#### **`data/external/`**

放外部数据库或第三方下载数据，比如 UniProt、GO、KEGG、Human Protein Atlas、dbPTM 等。

#### **`data/interim/`**

放中间文件，比如过滤后的临时表、初步合并表、还没有稳定下来的中间结果。

#### **`data/processed/`**

放已经可以被主分析流程稳定使用的数据。

例如：

```text
data/processed/
├── ptm_functional_sites.tsv
├── protein_embeddings.parquet
├── annotation_enrichment_table.parquet
└── sample_level_matrix.h5ad
```

#### **`data/metadata/`**

放样本信息、分组信息、批次信息、临床信息、实验设计表。

例如：

```text
data/metadata/
├── sample_info.tsv
├── batch_info.tsv
├── clinical_metadata.tsv
└── data_dictionary.md
```

对于生命健康项目，`metadata/` 的重要性不低于 raw data。很多分析错误都不是算法错误，而是样本分组、批次、命名、物种、时间点、组织来源搞错。

---

###  5.`configs/`：参数和路径独立出来

推荐结构：

```text
configs/
├── samples.yaml
├── parameters.yaml
└── paths.yaml
```

不要把参数散落在 notebook 或脚本中。

例如：

```yaml
# configs/parameters.yaml

embedding:
  model: pi-proteoformer
  dim: 1280
  normalize: true

retrieval:
  top_k: 50
  similarity: cosine

filter:
  min_confidence: 0.7
  remove_low_quality: true
```

好处是：同一个分析换参数时，不需要改代码，只需要改配置文件。

---

### 6. `code/`：代码分层

推荐结构：

```text
code/
├── notebooks/
├── scripts/
├── src/
├── workflows/
└── tests/
```

#### **`code/notebooks/`**

放探索性分析。

命名建议：

```text
01_data_overview.ipynb
02_quality_control.ipynb
03_main_analysis.ipynb
04_figure_generation.ipynb
```

或者加日期：

```text
2026-06-07_01_data_overview.ipynb
2026-06-08_02_embedding_retrieval_test.ipynb
```

Notebook 的原则是：

notebook 可以用于探索，但不要作为长期核心流程的唯一载体。

当 notebook 中某段代码稳定下来后，应迁移到 `scripts/` 或 `src/`。

#### **`code/scripts/`**

放可以直接运行的脚本。

例如：

```text
code/scripts/
├── build_annotation_table.py
├── run_retrieval.py
├── evaluate_model_outputs.py
└── generate_figures.py
```

#### **`code/src/`**

放可复用模块。

例如：

```text
code/src/
├── data_loader.py
├── annotation.py
├── retrieval.py
├── evaluation.py
├── visualization.py
└── utils.py
```

#### **`code/workflows/`**

放 Snakemake、Nextflow、Makefile 或 shell pipeline。

例如：

```text
code/workflows/
├── Snakefile
├── rules/
│   ├── preprocess.smk
│   ├── retrieval.smk
│   └── evaluation.smk
└── config.yaml
```

#### **`code/tests/`**

放最小测试，不一定要追求软件工程级别的高覆盖率，但关键函数要能测试。

例如：

```text
code/tests/
├── test_data_loader.py
├── test_annotation.py
└── test_retrieval.py
```

科研代码最需要测试的地方包括：

- 样本 ID 是否能正确匹配；
- 物种名称、蛋白 accession、基因名是否正确映射；
- 坐标、位点编号、修饰类型是否发生 off-by-one 错误；
- 过滤条件是否符合预期；
- 结果表的行数、列名、唯一性是否正常。

---

### 7. `ai_workflow/`：AI 工作流专用目录

这是传统目录结构中缺失、但现在非常重要的一部分。

推荐结构：

```text
ai_workflow/
├── prompts/
├── conversations/
├── agent_runs/
├── generated_code/
├── reviewed_outputs/
└── ai_notes.md
```

#### **`ai_workflow/prompts/`**

放稳定可复用的提示词。

例如：

```text
ai_workflow/prompts/
├── literature_summary_prompt.md
├── code_review_prompt.md
├── result_interpretation_prompt.md
├── ptm_reasoning_prompt.md
└── figure_caption_prompt.md
```

提示词不要只保存在聊天记录里。真正好用的 prompt 应该沉淀成项目资产。

#### **`ai_workflow/conversations/`**

放重要 AI 对话的导出或摘要。

例如：

```text
ai_workflow/conversations/
├── 2026-06-07_project_structure_discussion.md
├── 2026-06-08_ptm_agent_design.md
└── 2026-06-09_reviewer_response_brainstorm.md
```

不需要保存所有聊天。只保存对项目决策、分析路线、论文表达有价值的内容。

#### **`ai_workflow/agent_runs/`**

放 Agent 自动运行记录。

例如：

```text
ai_workflow/agent_runs/
├── 2026-06-07_run001/
│   ├── input.json
│   ├── output.json
│   ├── trace.json
│   ├── tool_calls.json
│   └── run_summary.md
└── 2026-06-08_run002/
```

如果你在做 PTM Agent、RAG、自动化筛选、文献阅读 Agent，这个目录非常重要。

建议每次 Agent 运行至少保留：

```text
input.json       # 输入是什么
output.json      # 输出是什么
trace.json       # 中间推理/工具调用轨迹，可脱敏
tool_calls.json  # 调用了哪些工具
run_summary.md   # 人工总结这次运行是否可信
```

#### **`ai_workflow/generated_code/`**

放 AI 生成但尚未人工确认的代码。

原则：

AI 生成的代码不要直接混入正式代码目录，必须经过 review 后再进入 code/。

例如：

```text
ai_workflow/generated_code/
├── 2026-06-07_build_faiss_index_draft.py
└── 2026-06-08_plot_umap_draft.py
```

#### **`ai_workflow/reviewed_outputs/`**

放已经人工核查过的 AI 输出。

例如：

```text
ai_workflow/reviewed_outputs/
├── 2026-06-07_literature_summary_checked.md
├── 2026-06-08_code_review_checked.md
└── 2026-06-09_result_interpretation_checked.md
```

建议所有用于论文、汇报、项目决策的 AI 输出，都经过人工核查后放入这个目录。

#### **`ai_workflow/ai_notes.md`**

记录 AI 在项目中的使用边界。

示例：

```markdown
# AI Usage Notes

本项目中 AI 工具主要用于：

1. 文献总结和研究思路整理；
2. 代码草稿生成和 debug；
3. 结果解释的初步归纳；
4. 图注、摘要、汇报文字润色；
5. Agentic screening 的流程自动化。

所有科学结论、统计分析、图表内容和论文表述均由作者人工核查。
AI 生成内容不得直接作为最终结论使用。
```

这对于未来论文、图注、审稿回复、AI 使用声明都很有帮助。

---

###  8. `results/`：分析结果，不等于论文结果

推荐结构：

```text
results/
├── exploratory/
├── tables/
├── figures/
├── models/
├── reports/
└── logs/
```

#### **`results/exploratory/`**

放探索性结果，不一定最终使用。

例如：

```text
results/exploratory/
├── 2026-06-07_first_qc/
├── 2026-06-08_embedding_test/
└── 2026-06-09_alternative_clustering/
```

#### **`results/tables/`**

放分析产生的结果表。

```text
results/tables/
├── ptm_site_annotation_summary.tsv
├── retrieval_top50_results.tsv
└── model_evaluation_metrics.tsv
```

#### **`results/figures/`**

放分析图，但不一定是最终论文图。

```text
results/figures/
├── qc_sample_distribution.pdf
├── retrieval_similarity_histogram.pdf
└── model_comparison_barplot.pdf
```

#### **`results/models/`**

放训练模型、checkpoint、embedding index 等。

```text
results/models/
├── faiss_index/
├── classifier_checkpoints/
└── calibration_models/
```

大模型 checkpoint 或大型索引通常不要进 Git，只保留路径说明和生成方式。

#### **`results/reports/`**

放自动生成的 HTML、Markdown 或 PDF 报告。

```text
results/reports/
├── 2026-06-07_qc_report.html
└── 2026-06-08_retrieval_evaluation.md
```

#### **`results/logs/`**

放运行日志。

```text
results/logs/
├── 2026-06-07_build_index.log
├── 2026-06-08_evaluate_model.log
└── failed_cases.log
```

---



### 9.`manuscript/`：最终交付物

推荐结构：

```text
manuscript/
├── figures/
├── tables/
├── supplementary/
├── drafts/
└── responses/
```

这里放的是面向论文、基金、汇报、审稿的最终材料，不要和 `results/` 混在一起。

关系应该是：

```text
results/figures/      # 分析过程中的图
manuscript/figures/   # 精修后准备投稿或汇报的图
```

例如：

```text
manuscript/figures/
├── Fig1_overview.pdf
├── Fig2_model_performance.pdf
├── Fig3_case_study.pdf
└── ExtendedData_Fig1_qc.pdf
```

---




### 10.`env/`：运行环境

推荐结构：

```text
env/
├── environment.yml
├── requirements.txt
├── Dockerfile
└── session_info/
```

建议至少保留一个 `environment.yml` 或 `requirements.txt`。

例如：

```yaml
name: ptm_rag
channels:
  - conda-forge
  - bioconda
dependencies:
  - python=3.10
  - pandas
  - numpy
  - scipy
  - scikit-learn
  - biopython
  - faiss-cpu
  - snakemake
  - pip
  - pip:
      - langchain
      - langgraph
```

对于重要结果，建议记录运行时环境：

```text
env/session_info/
├── 2026-06-07_python_packages.txt
├── 2026-06-07_conda_env_export.yml
└── 2026-06-07_gpu_info.txt
```

---

###  11.`references/`：文献和外部资料

推荐结构：

```text
references/
├── papers/
├── protocols/
└── resources.md
```

`resources.md` 可以记录重要链接：

```markdown
# Resources

## Project organization
- Bioinformatics project file management tutorial
- Good practice in computational biology
- Reproducible computational research

## Databases
- UniProt
- GO
- dbPTM
- Human Protein Atlas

## Tools
- Snakemake
- Nextflow
- FAISS
- Scanpy
```

不建议把所有论文 PDF 都复制很多份。更好的方式是用 Zotero 管理文献，项目目录中只放关键文献或链接说明。

---


### 12.`archive/`：归档，不是垃圾桶

推荐结构：

```text
archive/
├── old_results/
├── deprecated_code/
└── unused/
```

归档的原则：

- 不确定是否有用，但暂时不用的，放 archive；
- 已经确认错误的，不要只放 archive，要在文件名或 README 中说明；
- 大型旧结果可以压缩；
- 不要把 archive 当成第二个 results。

示例：

```text
archive/deprecated_code/
├── 2026-06-01_old_retrieval_pipeline_README.md
└── old_retrieval_pipeline.py
```

---

## **四、命名规范**

### **1. 总原则**

文件名应该满足：

```text
时间_对象_动作_版本.后缀
```

或者：

```text
项目_数据类型_分析内容_版本.后缀
```

推荐使用：

- 小写英文；
- 下划线 `_` 连接；
- 日期使用 `YYYY-MM-DD`；
- 避免空格；
- 避免中文文件名用于代码和数据；
- 论文草稿、汇报文档可以使用中文，但最好仍然有日期和版本。

---

### **2. 推荐命名示例**

#### **数据文件**

```text
sample_info_2026-06-07.tsv
ptm_sites_uniprot_raw_2026-06-07.tsv
ptm_sites_functional_processed_v1.tsv
protein_embeddings_pi_proteoformer_v1.parquet
```

#### **脚本文件**

```text
01_download_uniprot.py
02_build_annotation_table.py
03_run_retrieval.py
04_evaluate_results.py
05_generate_figures.py
```

#### **Notebook**

```text
2026-06-07_01_data_overview.ipynb
2026-06-08_02_embedding_retrieval_exploration.ipynb
2026-06-09_03_case_study_visualization.ipynb
```

#### **图表**

```text
fig1_project_overview_v1.pdf
fig2_model_performance_v2.pdf
extended_data_fig1_qc_metrics_v1.pdf
table1_dataset_summary_v1.xlsx
```

#### **AI 文件**

```text
2026-06-07_ptm_reasoning_prompt_v1.md
2026-06-07_agent_run001_summary.md
2026-06-08_literature_summary_checked.md
```

---

### **3. 不推荐命名**

```text
final.xlsx
final_final.xlsx
new_results.csv
test.py
plot.py
figure_new.pdf
改好的图.pdf
老师版本.docx
最终版2.docx
```

这些名字短期看方便，长期一定会造成混乱。

---

## **五、Git 管理建议**

Git 应该管理：

```text
README.md
project.yaml
docs/
configs/
code/
ai_workflow/prompts/
ai_workflow/reviewed_outputs/
env/
manuscript/drafts/
```

Git 不应该管理：

```text
data/raw/
data/processed/large_files
results/models/
large checkpoints
large embeddings
temporary logs
```

推荐 `.gitignore`：

```gitignore
# data
data/raw/
data/interim/
data/processed/*.h5ad
data/processed/*.parquet

# results
results/models/
results/logs/
results/exploratory/

# environment
.env
.venv/
__pycache__/
.ipynb_checkpoints/

# large files
*.bam
*.fastq
*.fastq.gz
*.mzML
*.raw
*.h5
*.h5ad
*.pt
*.pth
*.ckpt
*.faiss
```

如果需要管理大文件，可以考虑 Git LFS、DVC 或服务器路径记录，但不要把 Git 仓库变成数据仓库。

---

## **六、适合 AI 工作流的额外规则**

### **1. AI 生成内容要分级**

建议分为三类：

```text
draft      # AI 草稿，未核查
reviewed   # 已人工核查
final      # 可用于汇报/论文/交付
```

例如：

```text
ai_workflow/generated_code/     # draft
ai_workflow/reviewed_outputs/   # reviewed
manuscript/                     # final
```

### **2. AI 不能替代实验记录和分析记录**

AI 可以帮助总结、润色、生成代码、设计流程，但关键科学判断必须有人工确认。

尤其是这些内容不能只依赖 AI：

- 样本分组；
- 统计检验；
- 数据过滤标准；
- 图表含义；
- 论文中的科学结论；
- 审稿回复中的事实性表述；
- wet-lab validation 的描述。

### **3. Prompt 应该版本化**

如果一个 prompt 会反复用于文献总结、PTM 推理、Agent 筛选、结果解释，就应该保存到：

```text
ai_workflow/prompts/
```

并使用版本号：

```text
ptm_reasoning_prompt_v1.md
ptm_reasoning_prompt_v2.md
```

### **4. Agent 运行要保留 trace**

对于自动化 Agent，结果本身不够，还要保留：

- 输入；
- 工具调用；
- 中间证据；
- 输出；
- 人工评价；
- 是否进入正式结果。

否则后续很难判断 Agent 的结论是否可信。

---

## **七、面向你的实际项目的推荐简化版**

如果是你的 PTM_RAG、PTM_Agentic_Screening、SLOT、π-Proteoformer 这类项目，我建议使用下面这个精简但完整的模板：

```text
PROJECT_NAME/
├── README.md
├── project.yaml
├── docs/
│   ├── project_brief.md
│   ├── meeting_notes/
│   ├── literature_notes/
│   └── decisions.md
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
│   └── reviewed_outputs/
├── results/
│   ├── tables/
│   ├── figures/
│   ├── models/
│   └── logs/
├── manuscript/
│   ├── figures/
│   ├── tables/
│   ├── drafts/
│   └── supplementary/
└── env/
```

这个版本已经足够覆盖 90% 的科研项目，不需要一开始就做得更复杂。

---

## **八、一个新项目的启动流程**

每次新建项目，可以按以下步骤执行：

### **Step 1：建立目录**

```bash
mkdir -p PROJECT_NAME/{docs/{meeting_notes,literature_notes},data/{raw,processed,metadata},configs,code/{notebooks,scripts,src,workflows},ai_workflow/{prompts,agent_runs,generated_code,reviewed_outputs},results/{tables,figures,models,logs},manuscript/{figures,tables,drafts,supplementary},env}
touch PROJECT_NAME/README.md
touch PROJECT_NAME/project.yaml
touch PROJECT_NAME/docs/decisions.md
```

### **Step 2：写 README**

先写清楚：

- 项目要回答什么问题；
- 数据从哪里来；
- 主要分析路线是什么；
- 当前最重要的结果在哪里。

### **Step 3：整理 metadata**

先不要急着跑模型。先确认：

- 样本 ID；
- 分组；
- 批次；
- 物种；
- 组织；
- 时间点；
- 技术平台；
- 数据来源。

### **Step 4：写最小可运行流程**

先建立：

```text
code/scripts/01_prepare_data.py
code/scripts/02_run_main_analysis.py
code/scripts/03_generate_figures.py
```

即使一开始很粗糙，也比散落在 notebook 里更可控。

### **Step 5：沉淀 AI 工作流**

把重要 prompt 放进：

```text
ai_workflow/prompts/
```

把关键 AI 讨论放进：

```text
ai_workflow/conversations/ 或 ai_workflow/reviewed_outputs/
```

把 Agent 运行记录放进：

```text
ai_workflow/agent_runs/
```

---

## **九、最低限度规范**

如果时间很紧，不想维护太复杂的项目结构，至少保留下面这些：

```text
PROJECT_NAME/
├── README.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
├── code/
│   ├── notebooks/
│   └── scripts/
├── results/
│   ├── tables/
│   └── figures/
├── ai_workflow/
│   ├── prompts/
│   └── reviewed_outputs/
└── manuscript/
    ├── figures/
    └── drafts/
```

最低限度也要做到：

1. 原始数据不改；
2. metadata 单独放；
3. 代码和结果分开；
4. 每个重要结果知道由哪个脚本生成；
5. AI 生成内容和人工确认内容分开；
6. 最终论文图表和探索性结果分开。

---

## **十、我的建议**

我建议你不要把目录管理当成一个需要反复学习的“方法论问题”。对于你的工作流，更重要的是形成一个稳定的项目启动模板，然后在每个项目中复用。

真正值得投入精力的是以下三件事：

第一，建立统一的项目模板。每个新项目都从同一个目录结构开始，不要每次重新设计。

第二，维护 metadata 和 decisions。生命科学项目最容易出问题的是样本信息、分组、批次、版本和关键决策，而不是目录少了一个文件夹。

第三，把 AI 工作流纳入正式项目结构。AI 生成的 prompt、代码、Agent trace、结果解释和人工核查记录，都应该成为项目资产，而不是散落在聊天记录里。

对于你当前的科研类型，我推荐的最终原则是：

目录结构要服务于科学问题、复现路径和论文交付，而不是服务于形式上的整洁。  
足够清晰、足够可追踪、足够能让 AI Agent 读取和复用，就是一个好的科研项目目录。

我的额外判断是：你现在最需要的不是继续读更多“项目管理最佳实践”，而是把这个模板固化成一个 `create_project.sh` 或 Cookiecutter 模板。之后每个项目，比如 `PTM_RAG`、`PTM_Agentic_Screening`、`SLOT_analysis`、`pi_proteoformer_benchmark`，都用同一套结构启动。这样项目目录本身就会变成你未来 AI Agent 工作流的“操作系统”。