# T2：仓库骨架与页面初稿

## 目标

以 ci-policy 骨架为模板，搭出 stata-ai 全站结构并完成 P0 页面初稿，
本地 `quarto render` 无报错。

## 前置

T1 已完成并通过验收。所需输入：
- `_materials/harvest/`（T1 产出）
- `working/specs/outline-80min.md`（大纲内容）
- `working/specs/reading-links.md`（延伸阅读链接库）
- `_materials/blogs/`（3 篇推文，供改写）
- `_materials/misc/`（暑期班大纲、海报、报名二维码）

## 步骤

### 1. `.gitignore`（先做，防误推）

在仓库根目录写入（若已存在则合并）：

```
working/
_task/
_materials/
CLAUDE.md
.quarto/
/.claude/
*.stswp
```

注意：**不要**忽略 demo/，它是要发布的。写完执行 `git status` 确认上述目录已不在
未跟踪列表中。

### 2. `_quarto.yml`

以 `harvest/cipolicy/_quarto.yml` 为底本修改：

- 书名：`Stata 简介与 AI 辅助实证`；作者：连玉君（中山大学）；
- 仓库链接改为 `https://github.com/lianxhcn/stata-ai`；
- 章节结构：

```yaml
chapters:
  - index.qmd                 # 🏠 前言
  - outline.qmd               # 📌 课程大纲
  - settings.qmd              # 🚀 环境配置
  - part: "讲义"
    chapters:
      - lectures/01_stata_basics.qmd
      - lectures/02_vscode_nbstata.qmd
      - lectures/03_ai_vs_agent.qmd
      - lectures/04_agent_workflow.qmd
  - part: "附录"
    chapters:
      - appendix/A_prompt_templates.qmd
      - appendix/B_replication.qmd
      - appendix/C_more_usage.qmd
      - appendix/D_reading_list.qmd
```

- 样式：复用 harvest 里的 scss/css/include 文件，复制到本仓库同名位置；
- 发布方式：沿用 ci-policy 的设定；若其未指定 output-dir，则设 `output-dir: docs`。
- demo/ 与下划线开头目录不参与 render（Quarto 默认忽略 `_` 前缀；demo 若被卷入
  render 报错，在 project 配置中显式 exclude）。

### 3. 图片

`harvest/cipolicy/images/` 中的 logo、装饰线复制到 `images/`；
`_materials/misc/` 的海报与报名二维码复制到 `images/`（文件名改为 ASCII：
`poster-2026summer.png`、`qrcode-2026summer.png`）。

### 4. index.qmd（前言）

仿 ci-policy 前言的骨架，内容包含：

1. 课程信息：2026-07-12 19:30–21:00，主讲连玉君（中山大学）；
   直播入口留 `<!-- TODO: 直播/回放入口 -->`；
2. 「简介」：改写自 `_task/01-task-introduction.md` 附录中的公开课简介（两段版），
   不逐字照搬，压缩到 300 字内；
3. 一条主线（代码块呈现）：

```
研究问题 → 对话式 AI 拆解规划 → 任务说明书 → Agent 在项目中执行 → 人来检查与迭代
```

4. 「如何使用本仓库」：Fork/克隆方法；三类读者路径——只想配环境（→ settings）、
   想复现课堂演示（→ demo/ 下载后见其 README）、想系统学习（→ 7 月 21 日暑期初级班，
   插入海报图 + 报名二维码 + `_materials/misc/2026-暑期班-课程大纲.md` 中的报名链接）；
5. 页脚与 ci-policy 一致（主页/课程/推文/资料链接）。

### 5. outline.qmd（课程大纲）

内容 = `working/specs/outline-80min.md` 全文落地：模块时间表 + 各模块要点。
表格照搬，文字可润色。末尾加一句：讲义正文将在课后 3 日内持续更新。

### 6. settings.qmd（环境配置，全站最重要页面）

四节，每节末尾必须有「✅ 配置成功的标志」一行：

1. **Stata 本体与外部命令**：安装要点一笔带过（正版渠道链接），重点写
   `ssc install` 用法与常见失败处理；成功标志：`ssc install winsor2` 装上且
   `help winsor2` 能打开。改写素材：harvest/stata101 的 B4。
2. **VS Code + Stata 扩展 + nbstata**：VS Code 安装、Jupyter 扩展、nbstata 的
   pip 安装与内核配置。素材：harvest/ds2026（含 nbstata_hits）；若素材不足，
   按 nbstata 官方文档常规流程写，并标注 `<!-- TODO: 请老师验证步骤 -->`；
   成功标志：notebook 中 Stata 内核跑通 `sysuse auto, clear` + `summarize`。
3. **GitHub Copilot**：开通与 VS Code 登录；成功标志：注释触发出现灰色补全建议。
4. **Claude Code / Codex**：Windows 安装、首次运行、在 VS Code 终端中启动；
   成功标志：项目文件夹内启动后能列出文件清单。可引用 reading-links 中
   「Claude Code 协同 Stata」公开课链接作为深入配置指引。

### 7. lectures/ 四讲初稿

每讲结构固定：本讲回答的一个问题（一句话）→ 正文（600–1000 字初稿）→
课堂演示要点（列出将现场演示的操作）→ 延伸阅读（从 reading-links.md 选 3–5 条）。

- **01 Stata 最小入口**：素材 = harvest/stata101 的 B1/B2a/B6/B4 + blogs 的
  「优雅的实证研究」。覆盖：四个窗口、三行 dofile（use→summarize→regress）、
  help 的读法、ssc install、「永远用项目文件夹 + 相对路径」。
- **02 VS Code + nbstata + Copilot**：素材 = harvest/ds2026。覆盖：notebook 中
  笔记与代码同文件的价值、nbstata 运行、两个 Copilot 时刻（注释生成代码、
  代码生成注释）。
- **03 对话式 AI 与执行型 Agent**：素材 = blogs 的两篇分工文章（改写！）+
  harvest/cipolicy 的第 8 章。覆盖：两类工具的分工逻辑、任务说明书概念、
  「关键是搭配好环境、制定好计划」。本讲写厚一点（课上只有 7 分钟，仓库补足）。
- **04 Agent 工作流：从任务说明到结果检查**：覆盖：demo 项目的文件夹规范、
  计划→确认→执行→检查的循环、如何审查 agent 产出。末尾明确写：
  「下载本仓库 demo/ 文件夹，在其中启动 Claude Code 或 Codex，
  输入『请阅读 README.md 并先给出研究计划』，即可复现课堂演示。」

### 8. appendix/ 四个附录

- **A_prompt_templates.qmd**（P0 完成）：任务说明书写法要点 + 四个场景模板：
  ①数据清理与回归（即 demo README 的骨架化版本）②论文复现 ③概念学习/生成讲义
  ④模拟分析。素材：harvest/ds2026 的 a2/a3/a8 改写为 Stata 场景。
- **B_replication.qmd**（占位）：标题 + 一段说明「论文复现全记录，课后更新」。
- **C_more_usage.qmd**（占位）：模拟分析、AI 写讲义、从大压缩包提取数据三个小节
  的标题与一句话说明，注明课后补充截图。
- **D_reading_list.qmd**（P0 完成）：把 reading-links.md 全部条目按分组排版成页面。

### 9. render 与自检

`quarto render`，修复全部报错与坏链接；检查侧边栏结构、图片显示、页脚。

## 完成标准

- render 零报错；`git status` 干净（无 working/_task/_materials/CLAUDE.md）；
- 汇报：页面清单、遗留 TODO 列表；
- **停止，等待人工预览确认后进入 T3。**
