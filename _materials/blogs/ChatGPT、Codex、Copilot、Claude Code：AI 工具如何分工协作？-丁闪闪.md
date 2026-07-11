
> **作者：** 丁闪闪 (连享会)
> **邮箱：** [lianxhcn@163.com](mailto:lianxhcn@163.com)

&emsp;

- **分类**：AI 专题
- **Title**: ChatGPT、Codex、Copilot、Claude Code：AI 工具如何分工协作？
- **Keywords**: ChatGPT, Codex, Copilot, Claude Code, AI Agent, AI 编程, 项目工作流
- **提要**：本文分析了几个主流 AI 工具的分工协作关系：ChatGPT 适合讨论和判断，Codex 适合执行和交付，Copilot 适合即时补写，Claude Code 适合做第二个执行者或审稿人。通过合理搭配使用这些工具，可以大幅提升工作效率。
 
---

ChatGPT 能写作、解释、翻译、总结、画图；Codex 能进入项目文件夹，读取文件、修改代码、运行命令；Copilot 可以在 VS Code 中自动补写代码；Claude Code 也能处理代码库和多步任务。它们看起来功能重叠，但实际适用场景并不相同。

真正需要回答的问题不是「哪个工具最强」，而是「AI 工具应该如何搭配使用」：

* 一个任务应该放在对话框里完成，还是放进项目文件夹里完成？
* 哪些工作适合 ChatGPT，哪些工作适合 Codex？
* 有了 Codex，是否还需要 Copilot？
* Claude Code 是否值得继续保留？
* 如果已经购买 ChatGPT Plus、Pro、Copilot 或 Claude Code，怎样控制成本？
* ChatGPT 的图像生成能力和 Codex 的项目能力如何配合？

本文的基本判断是：**ChatGPT 适合讨论和判断，Codex 适合执行和交付，Copilot 适合即时补写，Claude Code 适合做第二个执行者或审稿人。** 它们不是简单替代关系，而是可以放进同一个工作流中的不同环节。

![ai\_tools\_fig01\_four\_ai\_tools\_division\_of\_labor](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/ai_tools_fig01_four_ai_tools_division_of_labor.png)

## 1. 先分清两类任务：对话任务和项目任务

使用 AI 时，很多低效并不是模型不够强，而是任务放错了地方。

有些任务适合在对话框中完成。例如，解释一篇论文的贡献，比较几种标题，修改一段文字，判断一个研究设计是否有识别风险，或者生成一张教学插图。这类任务的重点是理解、表达和判断，ChatGPT 很合适。

另一些任务更适合放到项目文件夹中完成。例如，修改一组 Markdown 文档，检查 Jupyter Notebook 代码，统一图片路径，重构 Python 项目，运行测试，或根据报错修改脚本。这类任务的重点不是继续对话，而是读取文件、执行修改和验证结果，Codex 更合适。

可以用一个简单标准判断：

> 如果任务主要发生在「脑子里」和「文字讨论中」，优先用 ChatGPT；如果任务已经落到「文件夹」和「代码库」里，优先考虑 Codex。

这一区分很关键。很多人觉得 AI 工具越用越乱，并不是因为工具太多，而是没有把任务拆成不同环节。一个任务还没想清楚时，就把它交给项目 Agent，往往会得到一堆看似完整但方向不准的修改；一个任务已经落到几十个文件里，却仍然用对话框反复复制粘贴，也会让人变成低效的文件搬运者。

## 2. ChatGPT 和 Codex 是什么关系？

ChatGPT 和 Codex 都是 OpenAI 的产品，但它们的产品形态不同。

ChatGPT 是通用对话入口。它适合用来讨论问题、生成文本、解释材料、审查思路、设计图示和组织表达。它的优势在于灵活：可以连续追问，也可以被当作写作助手、研究助手、教学助手或审稿人。

Codex 是面向项目执行的 coding agent。OpenAI 官方文档把 Codex 定位为 coding agent，可以在本地终端、IDE、Web 或 app 中使用，用来读取代码库、修改文件、运行命令和处理项目任务。换句话说，Codex 的价值不只是「会写代码」，而是能在一个项目环境中持续推进任务。

二者的差别可以概括为：

| 维度     | ChatGPT                      | Codex                        |
| -------- | ---------------------------- | ---------------------------- |
| 核心形态 | 对话助手                     | 项目执行 Agent               |
| 主要对象 | 问题、文本、材料、图片       | 文件夹、代码库、脚本、项目   |
| 擅长环节 | 理解、规划、表达、审稿、绘图 | 读取、修改、运行、检查、交付 |
| 典型问题 | 这件事该怎么想？             | 这个项目该怎么改？           |
| 使用方式 | 反复讨论和追问               | 分派任务并检查改动           |

因此，有了 Codex，并不意味着 ChatGPT 失去价值。相反，Codex 越适合执行，越需要 ChatGPT 帮助用户把任务定义清楚。

一个比较准确的说法是：

> ChatGPT 解决「如何理解」的问题，Codex 解决「如何落地」的问题。

## 3. 有了 Codex，还需要 ChatGPT 吗？

需要。二者不是替代关系，而是前后环节的关系。

ChatGPT 更适合做这些事：

* 把一个模糊任务拆成清楚任务；
* 判断文章、代码或研究方案的问题；
* 生成任务说明、写作提纲和审稿清单；
* 修改语言表达；
* 解释模型、公式、代码和结果；
* 生成概念图、讲义图和推文配图。

Codex 更适合做这些事：

* 在项目文件夹中批量修改文件；
* 读取代码库并解释结构；
* 修复脚本报错；
* 运行代码并检查输出；
* 根据任务说明修改 Markdown、Quarto、Notebook 或代码；
* 把图片、结果和文字整合进同一个项目。

更合理的用法是：

> ChatGPT 负责把任务想清楚，Codex 负责把任务做出来；ChatGPT 再负责审查 Codex 的结果。

比如，要写一篇包含论文解读、代码示例和配图的文章，不必一开始就让 Codex 直接输出全文。更稳的做法是先在 ChatGPT 中讨论文章定位、读者困惑、章节结构和实操部分，然后把这些要求整理成任务说明，再让 Codex 进入项目文件夹执行修改。最后，再回到 ChatGPT 检查文章是否清楚、是否有机器味、是否存在逻辑跳跃。

## 4. 如何让 ChatGPT 和 Codex 协作？

比较稳妥的流程是「规划—执行—审查」。

![ai\_tools\_fig02\_chatgpt\_codex\_workflow](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/ai_tools_fig02_chatgpt_codex_workflow.png)

可以把一次完整任务拆成四步。

1. **Step 1**: 用 ChatGPT 规划任务
   先让 ChatGPT 帮你判断任务边界。例如，这是一篇文章修改任务、代码调试任务、数据分析任务，还是项目重构任务。任务边界越清楚，后续 Codex 越不容易误改。

2. **Step 2**: 用 ChatGPT 生成任务说明
   把目标、输入文件、输出格式、修改边界、风格要求和验收标准写清楚。这个任务说明可以命名为 `to-codex-任务说明.md` 或 `AGENTS.md`。

3. **Step 3**: 让 Codex 在项目文件夹中执行
   Codex 按任务说明读取文件、修改文件、运行命令，并说明改了什么。复杂任务中，第一条指令最好不是「直接修改」，而是「先阅读项目结构并列出修改计划」。

4. **Step 4**: 回到 ChatGPT 做审稿
   让 ChatGPT 检查 Codex 的输出是否逻辑清楚、表达自然、代码与文字一致，是否存在遗漏或误改。

一个项目可以这样组织：

```text
project/
├── papers/
│   └── main-paper.pdf
├── drafts/
│   ├── old-version.md
│   └── final-version.md
├── code/
│   ├── analysis.py
│   └── example.do
├── figures/
│   ├── fig01.png
│   └── fig02.png
├── outputs/
│   └── results.txt
├── AGENTS.md
└── to-codex-任务说明.md
```

其中，`AGENTS.md` 可以写长期规则，例如写作风格、公式格式、链接格式、代码注释规范；`to-codex-任务说明.md` 则写本次任务的具体要求。长期规则和本次任务分开，Codex 更容易稳定执行。

例如，任务说明可以这样写：

```markdown
# to-codex-任务说明

## 任务目标

请基于项目文件夹中的论文 PDF、旧稿、代码和图片资料，修改并整合出一篇 Markdown 文章。

## 输入材料

- `papers/main-paper.pdf`: 论文原文
- `drafts/old-version.md`: 旧版草稿
- `code/example.do`: Stata 示例代码
- `outputs/results.txt`: 代码运行结果
- `figures/`: 已生成图片

## 输出要求

- 输出文件为 `drafts/final-version.md`
- 保留 Markdown 格式
- 全文控制在 6-8 个 sections
- 每个 section 要有明确问题意识
- 代码要有中文注释
- 结果解读要指出看哪一行、哪个系数或哪个图形

## 修改方式

- 请先阅读项目结构并列出修改计划
- 不要删除原始文件
- 修改前说明准备改哪些文件
- 修改后说明每个文件改了什么
```

这个流程的好处是，人不再在对话框和本地文件之间反复搬运内容，而是把 ChatGPT 和 Codex 放在不同环节中使用。

## 5. Codex、Copilot 和 Claude Code 如何分工？

Codex 出现后，不必立即取消 Copilot 或 Claude Code。它们虽然都能写代码，但工作方式不同。

Copilot 的优势是即时补写。你在 VS Code 中写代码时，它可以根据当前上下文补全下一行、一个函数或一段逻辑。它适合高频、轻量、低摩擦的代码输入。

Codex 的优势是项目执行。它更适合处理跨文件任务，例如重构项目、修复一组脚本、运行测试、合并文档和代码结果。

Claude Code 与 Codex 更接近，也适合处理代码库和多步任务。它的价值不一定在于替代 Codex，而在于作为第二个 Agent 或审稿人。对于复杂任务，可以让 Codex 和 Claude Code 分别给出方案，再人工比较；也可以让一个负责执行，另一个负责审查。

一个实用分工是：

| 工具        | 更适合的场景                             | 不宜强求的场景             |
| ----------- | ---------------------------------------- | -------------------------- |
| ChatGPT     | 讨论、规划、解释、写作、审稿、绘图       | 长期在本地项目中批量改文件 |
| Codex       | 项目修改、代码运行、文件整理、跨文件执行 | 替代所有非代码判断         |
| Copilot     | VS Code 中的即时补写                     | 独立管理复杂项目           |
| Claude Code | 复杂代码任务、交叉审核、第二套实现方案   | 所有小任务都双开           |

这里的关键不是「谁替代谁」，而是不要把所有任务都交给所有工具。小任务用一个工具即可；中等任务可以一个工具执行、另一个工具审稿；高风险任务才适合让两个 Agent 独立完成后再比较。

比如，写一个小函数时，Copilot 可能最快；整理一个项目时，Codex 更合适；担心 Codex 改错时，可以让 Claude Code 或 ChatGPT 做审查；需要改一篇文章的表达时，ChatGPT 通常比 coding agent 更自然。

## 6. 使用 Codex 是否需要额外付费？

这个问题需要分两层看。

按照 OpenAI 官方说明，ChatGPT Plus、Pro、Business、Edu 和 Enterprise 计划均已包含 Codex。但「包含」不等于「无限使用」。不同计划有不同额度，达到使用上限后，可以购买额外 credits 继续使用，或升级到更高计划。

关于计费方式，Codex 目前采用基于 token 的定价：credits 是购买和消耗的核心单位，但实际扣减按输入 token、缓存输入 token 和输出 token 分别计算。也就是说，消耗多少不再取决于「发了几条消息」，而是取决于每次任务实际用掉多少 token。此外，开启快速模式（Fast mode）会以更高速率消耗 credits，生成图片的消耗速度也比普通任务快约 3–5 倍。

因此，是否额外付费，不宜只看「我有没有 Plus」或「我有没有 Pro」，而应看实际任务强度。

可以粗略分成几类：

| 使用强度   | 典型任务                           | 可能选择                                       |
| ---------- | ---------------------------------- | ---------------------------------------------- |
| 轻度使用   | 偶尔改脚本、检查文档、处理小项目   | 先用现有 ChatGPT 计划，观察 token 消耗          |
| 中度使用   | 每周处理几次多文件任务或代码调试   | 观察额度消耗，再决定是否购买额外 credits        |
| 高强度使用 | 高频处理长代码库、大项目、云端任务 | 考虑更高额度计划，注意关闭不必要的 MCP 和快速模式 |
| 团队使用   | 多人协作、课程项目、机构项目       | 关注席位、权限、数据安全和管理功能             |

需要说明的是，AI 产品的费用和额度变化很快。文章、截图或他人经验很容易过期。实际使用时，应以账户中的 usage dashboard、官方 pricing 页面或命令行中的状态信息为准。

对大多数人来说，更稳妥的原则是：

> 先用现有计划跑通真实工作流，再根据额度消耗决定是否升级。

不要先为工具付费，再强行寻找使用场景。工具订阅越多，越需要用任务强度来约束成本。

## 7. ChatGPT Images 和 Codex 的图像能力怎么区分？

ChatGPT 的图像生成能力适合创作独立图片，例如推文封面、讲义插图、概念图、流程图和教学图示。它的重点是视觉表达。

Codex 也支持图像生成或编辑，但它更适合和项目结合使用。例如，为网页项目生成 banner、为应用生成占位图，或生成图片后直接接入项目文件。

可以这样理解：

> ChatGPT 适合「画一张图」；Codex 适合「把图放进项目里」。

如果目标是做文章配图、课程图示或概念解释图，优先用 ChatGPT。如果目标是给一个网页、应用或代码项目生成并接入图像资产，Codex 更方便。

实际工作中，二者可以配合使用。比如，先用 ChatGPT 生成两张教学图，再上传到图床；随后让 Codex 把图片链接插入 Markdown 正文，并在图片前后补充解释文字。这样，ChatGPT 负责图像表达，Codex 负责项目集成。

## 8. 使用这些工具时，最重要的是任务拆分

AI 工具越多，越容易陷入另一个误区：把工具比较当成主要问题。实际上，更关键的是任务拆分。

一个复杂任务通常包含几个环节：

* 理解问题；
* 设计方案；
* 修改文件；
* 运行代码；
* 检查结果；
* 优化表达；
* 生成图示；
* 发布交付。

ChatGPT、Codex、Copilot 和 Claude Code 可以分别进入不同环节，而不是在同一个环节重复消耗。

比较稳妥的规则是：

* 不清楚怎么做时，用 ChatGPT；
* 要改项目文件时，用 Codex；
* 正在写代码时，用 Copilot；
* 担心结果不可靠时，用 Claude Code 或 ChatGPT 交叉审核；
* 要生成独立图片时，用 ChatGPT Images；
* 要把图片接入项目时，用 Codex。

对复杂任务，还要注意三条操作原则。

**第一，先计划，再修改。** 让 Codex 或 Claude Code 先阅读项目结构并列出计划，不要一开始就直接大范围改文件。

**第二，小步修改，再统一检查。** 一次只改少数文件。先修复公式，再统一参考文献，再插入图片，再检查代码。小步修改更容易回滚。

**第三，高风险任务做交叉复核。** 涉及代码结果、论文事实、政策时间点、参考文献和收费规则时，不要只依赖一个 Agent。可以让另一个 Agent 审查，也可以人工核对官方来源。

## 9. 小结

Codex 的出现，并不意味着 ChatGPT 过时。它改变的是 AI 的工作位置：从对话框进入项目文件夹。

ChatGPT 仍然适合讨论、规划、写作、审稿和绘图；Codex 更适合执行项目任务；Copilot 适合代码即时补写；Claude Code 适合复杂任务和交叉审核。

更好的问题不是「哪个工具替代哪个工具」，而是：

> 这个任务应该在哪个环节完成？哪个工具最适合这个环节？

把这个问题想清楚，AI 工具才不会变成新的负担。

## 10. 相关资源

* [ChatGPT 官方页面](https://openai.com/chatgpt/)
* [Codex 官方页面](https://developers.openai.com/codex)
* [Codex CLI 文档](https://developers.openai.com/codex/cli)
* [Codex Pricing](https://developers.openai.com/codex/pricing)
* [Codex App Features](https://developers.openai.com/codex/app/features)
* [AGENTS.md 文档](https://developers.openai.com/codex/guides/agents-md)
* [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview)
* [GitHub Copilot Plans](https://github.com/features/copilot/plans)
* [Claude Code 文档](https://docs.claude.com/en/docs/claude-code)
* [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
* [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)

[1]: https://developers.openai.com/codex?utm_source=chatgpt.com "Codex | OpenAI Developers"
[2]: https://github.com/features/copilot?utm_source=chatgpt.com "GitHub Copilot · Your AI pair programmer"


&emsp;

## 11. 相关推文

> Note：产生如下推文列表的 Stata 命令为：   
> &emsp; `lianxh AI工具 ChatGPT Codex  Claude`  
> 安装最新版 `lianxh` 命令：    
> &emsp; `ssc install lianxh, replace` 

  - 丁闪闪, 2026, [AI 配图：彩色钢笔手绘风、白板风还是学术风？](https://www.lianxh.cn/details/1795.html).
  - 于凡, 2024, [AI可以编写Stata代码吗？](https://www.lianxh.cn/details/1348.html).
  - 余坚, 2023, [Stata：ChatGPT你能帮我干点啥？](https://www.lianxh.cn/details/1164.html).
  - 吴小齐, 2024, [强大的Kimi：中国版ChatGPT平替](https://www.lianxh.cn/details/1423.html).
  - 吴欣洋, 2025, [AI自动生成研究假设，靠谱吗？流程与挑战](https://www.lianxh.cn/details/1588.html).
  - 宗景辉, 2026, [GenAI 正在如何改变金融研究？一份系统性综述 (上)](https://www.lianxh.cn/details/1760.html).
  - 宗景辉, 2026, [GenAI 正在如何改变金融研究？一份系统性综述（下）](https://www.lianxh.cn/details/1762.html).
  - 宗景辉, 2026, [GenAI 正在如何改变金融研究？一份系统性综述（中）](https://www.lianxh.cn/details/1761.html).
  - 张弛, 2025, [找不到IV？如何借助大语言模型寻找工具变量](https://www.lianxh.cn/details/1575.html).
  - 林芷涵, 2026, [Claude Code Skills 写作指南：如何写好一个可复用的 SKILL.md](https://www.lianxh.cn/details/1791.html).
  - 王烨文, 2025, [LLM Agent：大语言模型的智能体图解](https://www.lianxh.cn/details/1650.html).
  - 王烨文, 2025, [Marker：高效 PDF 文档解析与结构化提取工具](https://www.lianxh.cn/details/1630.html).
  - 罗丹, 2025, [提示词！提示词！数据清洗、数据分析、可视化一网打尽](https://www.lianxh.cn/details/1638.html).
  - 艾米丽, 2026, [Claude 工程师力推 HTML 取代 Markdown，你怎么看？](https://www.lianxh.cn/details/1788.html).
  - 艾米丽, 2026, [从莫奈到梵高：实证图表中的配色学问](https://www.lianxh.cn/details/1779.html).
  - 董思源, 2025, [提示词！用 DeepSeek 快速生成更优代码](https://www.lianxh.cn/details/1569.html).
  - 赵文琦, 2025, [LLM系列：ChatGPT提示词精选与实操指南](https://www.lianxh.cn/details/1615.html).
  - 连享会, 2024, [AI编程助手大盘点：不止ChatGPT和Copilot](https://www.lianxh.cn/details/1394.html).
  - 连享会, 2025, [助教入选通知：2025 生成式人工智能专题](https://www.lianxh.cn/details/1677.html).
  - 连小白, 2025, [AI助手系列：napkin.ai-文字转换为图片和表格](https://www.lianxh.cn/details/1540.html).
  - 连小白, 2025, [AI助手系列：借助AI工具复现高质量图形](https://www.lianxh.cn/details/1584.html).
  - 连小白, 2025, [AI工具系列：英文学术论文语法检测与纠正](https://www.lianxh.cn/details/1562.html).
  - 连小白, 2025, [AI工具！AI工具分类大集合](https://www.lianxh.cn/details/1587.html).
  - 连小白, 2025, [No Chinglish：学术写作中的中式英语陷阱](https://www.lianxh.cn/details/1563.html).
  - 连小白, 2026, [从 Prompt 到 Skills：把论文复现、数据清洗和代码规范写进 AI](https://www.lianxh.cn/details/1790.html).
  - 连小白, 2025, [提示词来了！如何让 AI 翻译看起来像你写的](https://www.lianxh.cn/details/1640.html).
  - 连小白, 2026, [没有 Claude Code，如何实现 Skills？ChatGPT、DeepSeek、豆包](https://www.lianxh.cn/details/1794.html).
  - 连玉君, 2024, [VScode：实用 Markdown 插件推荐](https://www.lianxh.cn/details/1390.html).
  - 连玉君, 2024, [借助ChatGPT4o学习排序算法：AI代码助手好酸爽！](https://www.lianxh.cn/details/1393.html).
  - 连玉君, 2025, [如何借助 AI 工具来伴读一篇理论类的论文？](https://www.lianxh.cn/details/1571.html).
  - 连玉君, 2023, [连玉君：我与ChatGPT聊了一个月](https://www.lianxh.cn/details/899.html).
  - 邱一崎, 2025, [AITurk 平台论文复现](https://www.lianxh.cn/details/1534.html).
  - 郑怿轩, 2025, [40 个实证研究 AI 工具大集合](https://www.lianxh.cn/details/1666.html).
  - 陈庭伟, 2025, [2025年学术研究中的15大最佳AI工具](https://www.lianxh.cn/details/1578.html).
  - 颜国强, 2024, [ChatGPT争议：学术研究的加速器or信任危机的催化剂？](https://www.lianxh.cn/details/1421.html).
