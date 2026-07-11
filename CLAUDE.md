# CLAUDE.md — stata-ai 项目指南

> 本文件是本项目中 AI Agent（Claude Code / Codex）的总指南。开始任何工作前先读完本文件，
> 再按 `working/00-PLAN.md` 的流水线逐个执行任务。

## 1. 项目是什么

- 这是连玉君老师 2026-07-12 公开课「Stata 简介与 AI 辅助实证」的课程仓库。
- 用 Quarto book 编译，通过 GitHub Pages 发布，网址形如 https://lianxhcn.github.io/stata-ai 。
- 仓库有三重身份：课程主页、听众课后自学的配置手册、可下载复现的演示项目（demo/）。
- 风格基准：与 ci-policy 仓库（本地路径见 `_materials/三个仓库的本地路径.md`）保持一致——
  简体中文、导航结构、页脚 lianxh.cn 链接、克制的 emoji 使用。

## 2. 目录约定

```
stata-ai/
├── CLAUDE.md          # 本文件（不推送远程）
├── working/           # 过程文档：任务书、规格、真值记录（不推送远程）
├── _task/             # 老师自己的任务备忘（不推送远程）
├── _materials/        # 原始素材与收割文件（不推送远程）
├── _quarto.yml        # T2 生成
├── index.qmd 等       # T2 生成的正式页面
├── lectures/          # 四讲讲义
├── appendix/          # 附录 A-D
├── demo/              # 演示项目（T3 生成，随仓库发布）
└── images/            # 图片
```

**永远不推送远程的内容**：`working/`、`_task/`、`_materials/`、`CLAUDE.md`。
T2 任务中会写入 `.gitignore` 固化这条规则；任何 git 操作前先确认 `.gitignore` 生效。

## 3. 硬性规则

1. **中文写作**。全站简体中文；术语与命令名保留英文原文（如 dofile、csdid）。
2. **素材可直接使用**（`_materials/blogs/` 推文，以及 ci-policy、stata101、ds2026 三个
   仓库里的文字与图片，均为老师本人版权，无版权顾虑）：
   - **文字**：可直接采用，不必只做改写；觉得原文不够好时可自行改写、润色。
   - **图片**：直接复制原仓库 markdown 里的 `![text](url)` 图床链接使用，**不必**把图片
     文件另存到本仓库（图床 URL 版权同属老师）。
   - **链接**（作用类似论文参考文献，目的是让读者深入了解）：只截取段落性文字放入书稿时
     **不必**标注原文链接；截取后读者若需了解更深内容**可**附原文链接；涉及基础设施配置、
     软件安装等因 80 分钟课时**不便展开**的内容，**应**给出 ds2026 等仓库的完整链接，
     让读者按链接了解完整过程。
3. **不发明事实**。课程时间、价格、大纲等信息只能来自 `_materials/misc/` 中的文件；
   拿不准就留 `<!-- TODO -->` 注释并在任务结束时汇报。
4. **只读源仓库**。对 ci-policy、stata101、ds2026 三个本地仓库只有读权限，绝不修改。
5. **每个任务结束必须汇报**：做了什么、产出在哪、遇到什么问题、哪些 TODO 待人工确认。
   得到确认后才进入下一个任务。
6. `demo/_dgp/` 存放数据生成代码。在 T4 演示分析时，扮演分析者的 agent **不得读取**
   该文件夹与 `working/`（防止"偷看答案"），README 与任务提示词中已有约束。

## 4. 工具与环境

- 系统：Windows；在 VS Code 终端中运行。
- Quarto：用 `quarto render` 编译全站；报错先修复再继续。
- Stata：批处理模式调用，形如
  `"C:\Program Files\Stata19\StataMP-64.exe" /e do 文件名.do`。
  Stata 安装路径不确定时，先在 `C:\Program Files\` 下搜索 `Stata*`；找不到就停下来问人。
- 生成 PDF 用 Quarto 的 typst 引擎（免装 LaTeX），中文字体用 SimSun，详见 demo README。

## 5. 任务流水线（详见 working/00-PLAN.md）

| 任务 | 文件 | 执行者 |
|------|------|--------|
| T1 素材收割 | working/T1-harvest.md | Agent |
| T2 仓库骨架 | working/T2-skeleton.md | Agent |
| T3 demo 搭建 | working/T3-demo-build.md | Agent |
| T4 彩排预跑 | working/T4-rehearsal.md | 人主导 + Agent |
| T5 发布 | working/T5-publish.md | Agent |

一次只执行一个任务；执行前完整阅读对应任务书及其引用的 specs 文件。
