# T5：发布上线

## 前置

T4 已完成：demo/ 内已有 02_code、03_output、04_report（含 report.pdf）、logs 的
预跑成果，truth_comparison.md 就位。

## 步骤

### 1. 讲义收尾一处

在 `lectures/04_agent_workflow.qmd` 末尾补一小节「预跑成果」：链接 demo/ 内的
report.pdf 与 truth_comparison.md，并把对照表（TWFE vs csdid vs jwdid vs 真值）
以 Markdown 表格形式抄录进页面正文——这是听众课后最想看的一张表。

### 2. 发布前自检

- `quarto render` 零报错；
- `git status`：确认 working/、_task/、_materials/、CLAUDE.md 均未被跟踪；
  确认 demo/（含 CSV、代码、输出、logs、README）**已**被跟踪；
- 抽查编译产物中三个页面：index、settings、appendix D，链接可点、图片正常；
- demo/01_data 三个 CSV 合计大小应远小于 10 MB（GitHub 友好）。

### 3. 提交与推送

```
git add -A
git commit -m "feat: 公开课站点 v1（骨架 + demo + 预跑成果）"
git push origin main
```

### 4. GitHub Pages

若 T1 查明 ci-policy 用 GitHub Actions 发布且 workflow 已随骨架复制，则 push 后
检查 Actions 运行状态即可。否则（output-dir: docs 方案）打印以下步骤请人操作：
GitHub 仓库 → Settings → Pages → Source: Deploy from a branch →
Branch: main / docs → Save。

### 5. 验证

等待数分钟后访问 https://lianxhcn.github.io/stata-ai ，逐页抽查。
把最终网址与页面清单汇报给人，请人在手机端也打开确认一遍。

## 课后 P1 清单（备忘，另行安排）

- [ ] 四讲正文充实（每讲 1500–2500 字 + 截图）
- [ ] 附录 B：Energy Economics 论文复现全记录（指令原文、执行计划、结果对照、问题记录）
- [ ] 附录 C：模拟分析、AI 写讲义、大压缩包提取数据的成品截图
- [ ] 公众号/群内发布「讲义已更新」二次触达
