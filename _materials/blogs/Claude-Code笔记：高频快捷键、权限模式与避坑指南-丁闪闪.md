
> **作者：** 丁闪闪 (连享会)
> **邮箱：** <lianxhcn@163.com>

&emsp;

- **分类**：AI 专题
- **Title**: Claude-Code笔记：高频快捷键、权限模式与避坑指南
- **Keywords**: Claude Code, AI Agent, VS Code, 快捷键, 权限模式, 上下文管理

---

![Claude Code：AI Agent 进入研究项目工作流](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/claude-code-01-workflow-overview.png)

或许很多人都有这样的感受：使用 [Claude Code](https://code.claude.com/docs/en/overview) 网页版感觉很简单。听闻 Agent 模式可以让 AI 直接在本地项目文件夹里工作。然而，等真正在本地项目里操作时，你会发现情况没那么简单 —— 感觉无从下手，自己似乎指挥不了这个 Agent。常见问题包括：

- 我怎们让 Agent 知道我的项目结构和规则？
- Agent 不停地问我：要继续吗 (`1. Yes`)？我感觉自己还要像个老妈子一样盯着它每一步操作。
- 不小心下达了错误的命令，看着它在错误的道路上狂奔，却不知道该如何停止和回退。
- Claude 占用了终端，导致我无法在终端里执行其他命令。
- ……

本文从一个新手的视角出发，讲述如何在本地项目中使用 Claude Code，让 AI 高效地参与项目工作。文中介绍的所有快捷键和命令均以 [官方 Interactive Mode 文档](https://code.claude.com/docs/en/interactive-mode) 为准；Claude Code 更新很快，不同版本的提示文字和快捷键可能略有出入，遇到对不上的地方，在会话中按 `?` 或输入 `/help` 查看当前版本的说明。

## 1. 先理顺工作方式：文件夹即工作区

![Claude Code：从聊天窗口进入项目工作区](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/claude-code-02-project-workspace.png)

Claude Code 不需要额外「绑定」项目：在哪个文件夹里启动，它就以哪个文件夹为工作区。在 VS Code 中用 `` Ctrl+` `` 打开集成终端（此时终端已自动定位在项目文件夹），输入 `claude` 即可开始。

新项目的第一步是输入 `/init`。它会扫描项目结构，自动生成一份 `CLAUDE.md`——这是 Claude Code 每次启动都会自动读取的「项目记忆」，项目背景、文件夹用途、工作规则都写在这里。每次启动 Claude Code 时，它都会读取这个文件，以便在对话中保持上下文一致。

>Note： 
1. 如果你此前已经在 ChatGPT 或 Claude code 网页端进行了项目规划，并在项目文件夹中生成了 `CLAUDE.md` 文件，则无需再次初始化，Claude Code 会读取已有的 `CLAUDE.md` 文件。
2. 如果你在项目中修改了 `CLAUDE.md`，需要重新启动 Claude Code 或在会话中让它重新读取该文件，否则对话中的上下文不会更新。

日常对话中，有三个前缀符号使用频率极高：

| 前缀 | 作用                               | 示例                                |
| :--- | :--------------------------------- | :---------------------------------- |
| `@`  | 引用文件或目录，让 Claude 精准定位 | `@plans/本周任务.md 开始做第一项`   |
| `#`  | 把一条规则永久写入记忆文件         | `# 所有输出文件统一放 output/ 目录` |
| `!`  | 直接执行 shell 命令，不经过 AI     | `! git status`                      |

一个容易忽略的细节：`CLAUDE.md` 每轮对话都会被读取，写得越长，消耗的上下文越多。建议只放「永远需要知道」的规则，控制在百行以内，细节资料用 `@` 按需引用。

## 2. 权限模式：Shift+Tab 是最重要的一个快捷键

![Claude Code：权限模式与推荐工作流程](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/claude-code-03-permission-mode.png)

Claude Code 的权限模式决定了它在本地项目中能否直接修改文件。不同模式下，它的行为不同，按 `Shift+Tab` 可以循环切换模式，你可以在输入框下方的状态栏中看到如下几种模式：

```text
II plan mode on (shift+tab to cycle)
II manual mode on • ← for agents
» auto mode on (shift+tab to cycle)
» accept edits on (shift+tab to cycle)
```

| 模式     | 状态栏关键词   | 行为                                   | 适用场景             |
| :------- | :------------- | :------------------------------------- | :------------------- |
| 默认模式 | 无特殊标记     | 每次改文件、跑命令前都征求同意         | 刚上手；改动敏感资料 |
| 自动接受 | `accept edits` | 文件编辑直接执行，敏感命令仍会询问     | 批量、重复性修改     |
| 计划模式 | `plan mode`    | 只读不写：先分析、出方案，经确认再动手 | 复杂任务开工之前     |

推荐的节奏是：

- 复杂任务先切到**计划模式**，让它读项目、列出行动方案，你审阅修改后再放行；
- 方案确定后切**自动接受**批量执行；
- 若涉及重要内容或敏感性较高的改动，切回**默认模式**逐项过目。

两点提醒。其一，部分 Windows 版本存在 `Shift+Tab` 跳过计划模式的已知问题，此时可直接输入 `/plan` 进入。其二，还有一档「跳过所有确认」（bypass permissions），需要启动时特意开启，任何操作都不再询问——除非在隔离的测试环境，否则不建议使用。

## 3. 高频快捷键：这几个先形成肌肉记忆

快捷键很多，但新手真正每天用到的是下面这些：

| 快捷键                         | 作用                                             |
| :----------------------------- | :----------------------------------------------- |
| `Esc`（按一次）                | 打断正在执行的任务，已完成的部分保留             |
| `Esc` + `Esc`（连按两次）      | 打开「回退」菜单，把代码和对话恢复到之前的检查点 |
| `Shift+Tab`                    | 循环切换权限模式                                 |
| `\` + `Enter`                  | 输入换行（多行提示词），任何终端都有效           |
| `Ctrl+R`                       | 搜索历史输入，翻旧提示词不用一路按上箭头         |
| `Ctrl+V`（Windows 为 `Alt+V`） | 把剪贴板里的截图直接粘贴给 Claude                |
| `Ctrl+G`                       | 在外部编辑器中撰写长提示词，保存即发送           |
| `?`                            | 查看当前版本的全部快捷键                         |

其中 `Esc Esc` 值得单独强调：它不是简单的「停止」，而是回滚——Claude 改了一堆文件后你发现方向错了，连按两次 `Esc` 选择恢复到之前的状态，比手动撤销省事得多。发现它改错时，不要等它做完，先 `Esc` 打断、说清要求，必要时回退。

Mac 用户注意：涉及 `Option` 键的快捷键需要先在终端里把 Option 配置为 Meta 键；VS Code 用户在设置中加入 `"terminal.integrated.macOptionIsMeta": true`。想用 `Shift+Enter` 换行的话，在会话里运行一次 `/terminal-setup` 即可完成绑定。

## 4. 上下文管理：新手最大的痛点

![Claude Code：上下文管理与清理流程](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/claude-code-04-context-management.png)

社区里被抱怨最多的现象是：一开始对答如流，越到后面越糊涂——忘记之前说好的规范、反复犯同样的错、甚至把刚改好的代码又改回去。这不是模型「变笨」，而是上下文窗口快满了。长对话还会连带另一个代价：每轮请求都携带全部历史，token 消耗和费用同步上涨。

应对思路是「精简噪音，保留信号」，三个命令要会用：

- `/context`：查看当前上下文占用了多少，心里有数；
- `/compact`：把对话历史压缩成摘要，腾出空间。进阶用法是带指令的定向压缩，例如 `/compact 保留引用格式的修改规则，省略调试细节`，摘要的信噪比会高得多；
- `/clear`：清空上下文，重开一个话题。

很多人舍不得用 `/clear`，怕丢了上下文。实际上，任务切换处主动清空，往往比带着「脏上下文」继续更高效——尤其当系统已经第二次自动触发压缩时，早期细节多半已经丢失，与其在残缺摘要上继续，不如 `/clear` 后用一段话重述任务。真正需要长期记住的信息，应该用 `#` 写进 `CLAUDE.md`，而不是指望对话历史。

Stata 用户尤其要留意一个概念区分：`/clear` 不是 `cls`。Stata 的 `cls` 是纯视觉操作，只擦掉结果窗口的显示，内存中的数据和暂元原封不动；而 `/clear` 清掉的是模型的「工作记忆」——执行之后 Claude 真的不记得这场对话说过什么了，需要重新交代任务背景，屏幕变干净只是附带效果。用 Stata 的概念对应如下：

| Stata                   | Claude Code              | 效果                   |
| :---------------------- | :----------------------- | :--------------------- |
| `cls`                   | `Ctrl+L`                 | 只清屏幕显示，记忆不动 |
| `clear`（清空内存数据） | `/clear`                 | 清空工作记忆，从头开始 |
| 磁盘上的 dta / log 文件 | `~/.claude` 中的会话记录 | 均不受影响，可随时调出 |

也就是说，只是嫌屏幕太乱、想擦干净接着聊，用 `Ctrl+L`；`/clear` 则是「内存清空、轻装上阵」。且与 Stata 的 `clear` 一样，它动的只是内存：硬盘上的会话记录还在（`/resume` 或 `claude --resume` 可从历史列表中恢复任意一段旧对话），Claude 此前对项目文件的修改也都落在磁盘上，不会被撤销——想回退文件改动，那是 `Esc Esc` 或 Git 的事。

退出也不会丢进度：`/exit` 关闭后，随时可以用 `claude -c` 恢复上一次对话。担心额度的话，`/usage` 可查看订阅用量，API 计费用户可用 `/cost` 查看本次会话的开销。

## 5. 与 VS Code 的配合

![Claude Code、VS Code、Git 与项目文件的协作闭环](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/claude-code-05-tool-loop.png)

官方 VS Code 扩展提供两种形态：图形化面板（默认）和集成终端里的命令行。两者功能大体一致，图形面板对新手更友好——修改以 diff 对比视图呈现，接受或拒绝一目了然；命令行则功能最全，部分高级命令只在 CLI 中可用。

几个 VS Code 场景下的专属技巧：

- `Ctrl+Esc`（Mac 为 `Cmd+Esc`）：在代码编辑器和 Claude 输入框之间切换焦点；
- `Alt+K`（Mac 为 `Option+K`）：把当前选中的代码以 `@file.ts#5-10` 的形式插入提示词，精确到行号；
- 在终端版会话里输入 `/ide`：把当前会话挂接到 VS Code，代码改动改在编辑器的 diff 视图中高亮显示，Claude 还能读取你的光标选区和 linter 报错；
- 布局上，建议 Claude 独占一个终端或面板，自己跑命令另开一个终端（`` Ctrl+Shift+` ``），互不干扰。

无论哪种形态，都要养成同一个习惯：**不要只看 AI 的解释，要看它实际改了什么**。左侧文件树会实时刷新，配合 Git 的变更标记，每轮修改后花半分钟核对 diff，是成本最低的质量保险。

## 6. 避坑清单

把社区反馈和个人体会汇总成一张表，供对照自查：

| 常见坑                   | 症状                           | 对策                                        |
| :----------------------- | :----------------------------- | :------------------------------------------ |
| 一直用默认模式跑批量任务 | 每改一个文件都要确认，效率极低 | `Shift+Tab` 切自动接受，配合 Git 兜底       |
| 复杂任务直接开干         | 改了一半发现方向不对           | 先进计划模式，方案确认后再执行              |
| 舍不得清空对话           | 越聊越糊涂、token 烧得飞快     | 任务边界处 `/clear`；长期规则进 `CLAUDE.md` |
| 改错了才想起没退路       | 手动一个个文件撤销             | 项目先 `git init`；善用 `Esc Esc` 回退      |
| 长时间无人监督地自动运行 | 一觉醒来额度见底、产出难用     | 大任务拆步骤，每步核对后再继续              |
| 敏感资料不设防           | 未公开数据、密钥被读取或上传   | 敏感内容移出工作区；改动前要求先出计划      |

最后再强调一次版本问题：Claude Code 几乎每周都在更新，模式名称、快捷键、默认行为都可能调整。本文写作时以官方文档为准核对过一遍，但你阅读时未必如此——拿不准时，`?` 和 `/help` 永远是最可靠的答案。

## 7. 参考资料

- Anthropic. (2026). Claude Code overview. [Link](https://code.claude.com/docs/en/overview), [Quickstart](https://code.claude.com/docs/zh-CN/quickstart), [Google](https://scholar.google.com/scholar?q=Claude+Code+agentic+coding+tool).
- Anthropic. (2026). Claude Code interactive mode. [Link](https://code.claude.com/docs/en/interactive-mode), [Google](https://scholar.google.com/scholar?q=Claude+Code+interactive+mode+keyboard+shortcuts).
- Anthropic. (2026). Claude Code in VS Code. [Link](https://code.claude.com/docs/zh-CN/vs-code), [Google](https://scholar.google.com/scholar?q=Claude+Code+VS+Code+extension).
- Anthropic. (2026). Claude Code cheatsheet. [Link](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet), [Google](https://scholar.google.com/scholar?q=Claude+Code+cheatsheet).
- Kiddyup. (2026). Claude Code 上下文管理实践. [Link](https://blog.csdn.net/Kiddyup/article/details/158888672), [Google](https://scholar.google.com/scholar?q=Claude+Code+context+management).
- Automate and Tweak. (2026). How to use plan mode in Claude Code (VS Code). [Link](https://medium.com/@automateandtweak/how-to-use-plan-mode-in-claude-code-vs-code-the-smart-way-to-code-with-ai-a93d1b437646), [Google](https://scholar.google.com/scholar?q=Claude+Code+plan+mode).

## 8. 相关推文

> Note：产生如下推文列表的 Stata 命令为：
> &emsp; `lianxh claude code agent, md2 nocat`
> 安装最新版 `lianxh` 命令：
> &emsp; `ssc install lianxh, replace`

- 丁星星, 2026, [从代码补全到 AI Agent：Copilot、Cursor、Claude Code、Codex 怎么选？](https://www.lianxh.cn).
- 连享会, 2026, [公开课：Claude Code 协同 Stata：环境配置与应用实践](https://www.lianxh.cn/details/1767.html).
- 林芷涵, 2026, [Claude Code Skills 写作指南：如何写好一个可复用的 SKILL.md](https://www.lianxh.cn/details/1791.html).
- 连小白, 2026, [从 Prompt 到 Skills：把论文复现、数据清洗和代码规范写进 AI](https://www.lianxh.cn/details/1790.html).
- 丁闪闪, 2026, [AI我知道-01：AI 怎么读懂你的话？Token、上下文窗口与提示词](https://www.lianxh.cn/details/1770.html).
- 丁闪闪, 2026, [AI我知道-04：AI 如何自己干活?Agent、工具调用与 MCP](https://www.lianxh.cn/details/1774.html).
