# Manage AI Research Projects

语言：[English](README.md) | 简体中文

`manage-ai-research-projects` 是一个用于管理 AI 时代计算科研项目的 Agent Skill。它可以帮助 Claude Code、Codex 以及其他兼容 Agent Skills 的智能体创建可复现的项目结构，审计已有项目，区分 AI 生成草稿和人工核查产物，并让科研结果能够追溯到数据、代码、参数、运行环境、关键决策和论文交付材料。

这个 skill 基于一个轻量级科研项目管理模板，适合计算生物学、生物信息学、AI 辅助科研工作流、RAG/agentic screening 项目、模型 benchmark，以及面向论文或汇报交付的分析项目。

## 仓库结构

```text
.
└── manage-ai-research-projects/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/
    └── scripts/
```

真正可安装的 skill 包是 `manage-ai-research-projects/` 目录。

## 安装

### Claude Code

安装为个人 skill：

```bash
mkdir -p ~/.claude/skills
cp -R manage-ai-research-projects ~/.claude/skills/
```

或者只安装到某一个项目中：

```bash
mkdir -p .claude/skills
cp -R manage-ai-research-projects .claude/skills/
```

在 Claude Code 中可以直接调用：

```text
/manage-ai-research-projects
```

### Codex

安装为个人 Codex skill：

```bash
mkdir -p ~/.codex/skills
cp -R manage-ai-research-projects ~/.codex/skills/
```

之后可以让 Codex 使用 `$manage-ai-research-projects`。

## 从 GitHub 使用

用户可以下载仓库 ZIP，或者 clone 仓库，然后把 `manage-ai-research-projects/` 目录复制到对应智能体的 skills 目录。

示例：

```bash
git clone https://github.com/Devin-jun/Manage-AI-Research.git
cp -R Manage-AI-Research/manage-ai-research-projects ~/.claude/skills/
```

## 功能

- 创建简化的科研项目骨架，包括 `README.md`、`project.yaml`、data/code/results/manuscript 目录和 AI 工作流记录。
- 审计已有项目，检查 metadata 缺失、复现性薄弱、结果追踪不清、文件命名模糊、AI 草稿和正式输出混杂等问题。
- 将原始数据作为不可变资产管理，并与处理后的分析数据分开。
- 将 AI 生成代码、提示词、agent 运行轨迹和人工核查输出放在不同位置。
- 将最终论文或汇报材料与探索性分析结果分开，方便后续交付。

## 本地验证

在临时目录中测试项目初始化脚本：

```bash
python3 manage-ai-research-projects/scripts/init_research_project.py demo_project --root /tmp --title "Demo Project"
```

审计生成的项目：

```bash
python3 manage-ai-research-projects/scripts/audit_research_project.py /tmp/demo_project
```

检查 Python 语法：

```bash
PYTHONPYCACHEPREFIX=/tmp/skill_pycache python3 -m py_compile \
  manage-ai-research-projects/scripts/init_research_project.py \
  manage-ai-research-projects/scripts/audit_research_project.py
```

## 发布说明

如果提交到 skill registry 或 skill hub，指向可安装的 skill 目录：

```text
manage-ai-research-projects/
```

这个 skill 遵循 Agent Skills 的常见目录约定：

```text
skill-name/
├── SKILL.md
├── scripts/
└── references/
```

`agents/openai.yaml` 是可选的 Codex 元数据，不影响 Claude Code 兼容性。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
