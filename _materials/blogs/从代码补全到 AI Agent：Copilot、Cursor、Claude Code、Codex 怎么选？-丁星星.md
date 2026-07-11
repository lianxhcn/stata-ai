
> **作者：** 丁星星 (连享会)    
> **邮箱：** <lianxhcn@163.com> 

&emsp;

- **分类**：AI 专题
- **Title**: 从代码补全到 AI Agent：Copilot、Cursor、Claude Code、Codex 怎么选？
- **Keywords**: AI 编程工具, 智能体, 代码编辑器, 终端 Agent, 任务代理

---


![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/lianxh_ai_agent_tools_fig01_cover.png)

现在很多人已经开始用 AI 写代码。刚开始看起来很简单：打开一个工具，告诉它「帮我改代码」，它就会自动解释报错、补全函数、修改脚本，甚至帮你整理整个项目。

真正用起来后，问题很快出现：[GitHub Copilot](https://github.com/features/copilot/plans)、[Cursor](https://cursor.com/)、[Claude Code](https://code.claude.com/docs/en/overview)、[Codex](https://chatgpt.com/codex/)，到底应该选哪个？有的装在 VS Code 里，有的本身就是一个编辑器，有的要在终端运行，有的可以连接 GitHub 仓库。有的按月订阅，有的按 credits 扣费，有的还需要配置 API key。

这篇文章不做排行榜。因为这些工具本来就不是同一类东西。对多数使用者来说，更重要的问题不是「哪个最强」，而是：

> 我的任务现在处在哪一步？我希望 AI 帮我做到什么程度？

如果只是写一小段 Python 代码，用代码补全工具就够了。如果已经有一个课程项目、论文复现项目或本地代码文件夹，就需要能读项目、改文件、跑命令的 Agent。如果已经有 GitHub 仓库、issue、测试和多人协作需求，才需要更完整的云端任务代理。

## 1. AI 编程工具的主要类型

把常见 AI 编程工具放在一起看，大致可以分成四类：

| 类型          | 典型工具                   | 主要功能                 |
|:------------- |:---------------------- |:------------------------ |
| 代码补全型    | [GitHub Copilot](https://github.com/features/copilot/plans) | 写代码时的实时助手       |
| AI IDE 型     | [Cursor](https://cursor.com/)                               | 带 AI 的代码编辑器       |
| 终端 Agent 型 | [Claude Code](https://code.claude.com/docs/en/overview)     | 本地项目里的结对程序员   |
| 任务代理型    | [Codex](https://chatgpt.com/codex/)                         | 可以接收代码任务的 Agent |

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/lianxh_ai_agent_tools_fig02_tool_roles.png)

这四类工具的边界不是绝对的。现在很多产品都在向 Agent 演化：`Copilot` 不再只是补全，`Cursor` 也能运行 Agent，`Codex` 既可以在本地 [Codex CLI](https://github.com/openai/codex) 中使用，也可以通过 [Codex Web](https://developers.openai.com/codex/cloud) 连接云端环境和 GitHub 工作流。

但对刚开始使用 AI 编程工具的人来说，先把这四类区分开很有必要。否则很容易出现两种误解。

一种误解是把所有 AI 编程工具都当成「更聪明的 ChatGPT」。于是把一大段报错复制进去，期待它直接给出最终答案。短代码可以这样做，真实项目通常不行。

另一种误解是以为最贵、最强、最 Agent 的工具一定最适合自己。事实上，很多代码问题还停留在「路径不对」「包没装好」「函数名写错」「不知道该看哪个文件」。这类问题不一定需要完整 Agent，一个稳定的编辑器助手反而更合适。

选择 AI 编程工具，不是选一个模型，而是选一个工作流。

## 2. Copilot：代码生成和补全

[GitHub Copilot](https://github.com/features/copilot/plans) 是很多人最早接触的 AI 编程工具。它最典型的使用方式是在 VS Code、JetBrains 或 GitHub 环境中，根据上下文自动补全代码，也可以通过 chat 解释代码、生成函数、回答报错问题。

它适合的场景很清楚：你正在写代码，但不知道下一行怎么写。

例如，已经知道自己要做什么，只是不熟悉语法：

```python id="qez1um"
# 读取 wage.csv
# 按 industry 分组，计算 wage 的均值
# 画出各行业平均工资的柱状图
```

写出这几行注释后，`Copilot` 往往可以补出基本代码。使用者再根据实际数据列名和输出效果做调整。

这类工具的好处是干预程度低。它不会一上来重构整个项目，也不会在你没看清楚的情况下改十几个文件。对刚开始学习 Python、R 或 Stata 的人来说，这反而是优点。你仍然在写代码，AI 只是帮你补语法、补模板、解释错误。

它特别适合：

* 课程作业；
* 小函数、小脚本；
* 数据读取和简单清洗；
* 图表绘制；
* 语法补全；
* 简单报错解释。

但它也有明显边界。`Copilot` 不适合让人完全不看代码，只说「帮我把这个项目跑通」。它可以辅助写代码，但不等于自动完成科研项目。

对初学者来说，`Copilot` 的正确用法不是「替我写完」，而是「我写一个方向，你帮我补下一步」。使用者仍然要看懂每一行代码，知道输入是什么、输出是什么、哪里可能错。

费用和权益方面，`Copilot` 有免费版、个人版和团队版等不同计划。使用前应直接查看 [GitHub Copilot Plans & Pricing](https://github.com/features/copilot/plans) 和 [GitHub Copilot Plans 文档](https://docs.github.com/en/copilot/get-started/plans)。需要说明的是，注册开放状态、免费权益和 credits 规则变化较快，不宜只依据旧教程判断当前是否还能免费使用。

## 3. Cursor：在编辑器里读项目、改项目

如果说 `Copilot` 更像「写下一行代码的助手」，那么 [Cursor](https://cursor.com/) 更像「带 AI 的代码编辑器」。它基于编辑器工作流，适合打开一个项目文件夹，让 AI 读取多个文件、解释项目结构、修改局部代码。

假设一个项目长这样：

```text id="2vzgwh"
paper-project/
├─ data/
├─ code/
├─ results/
├─ figures/
└─ README.md
```

可以在 `Cursor` 中提出更接近项目级的问题：

```text id="wemgwr"
请阅读这个项目，说明每个文件夹的作用。
检查 code 目录下哪些脚本使用了绝对路径。
把所有输出图形统一保存到 figures 文件夹。
```

这类任务已经超出「补全下一行代码」的范围。它需要 AI 理解多个文件之间的关系，知道哪个脚本读入数据，哪个脚本生成回归表，哪个文件保存图形输出。

`Cursor` 的优点是使用门槛相对低。它仍然是编辑器，不要求一开始就熟练使用终端、Git 或命令行。你打开项目，选择文件，提问题，看修改，接受或拒绝建议。这种工作流比较符合多数人的使用习惯。

它适合：

* 阅读陌生项目；
* 修改已有代码；
* 解释函数和脚本；
* 批量替换路径；
* 整理输出目录；
* 补充 `README.md`；
* 生成简单测试或示例。

需要提醒的是，`Cursor` 改文件很方便，也正因为方便，使用者更要学会看 `diff`。所谓 `diff`，就是修改前后代码的差异。AI 建议改哪里、删哪里、加哪里，必须看清楚再接受。

这也是开始使用 AI 编程工具后必须养成的第一个习惯：

> 不要只看 AI 的解释，要看它实际改了什么。

如果你还不会判断代码是否被改坏，就不要一次性让 AI 修改太多文件。让它先说明计划，再分步修改，会更稳。

费用方面，`Cursor` 当前有 Hobby、Individual、Teams、Enterprise 等不同计划，具体权益和 usage-based pricing 规则应查看 [Cursor Pricing](https://cursor.com/pricing)。免费版适合试用，付费版是否值得取决于你是否已经在真实项目里持续使用 Agent。

## 4. Claude Code：适合本地科研项目和可复现代码

[Claude Code](https://code.claude.com/docs/en/overview) 更接近终端中的结对程序员。它的典型使用方式是：进入一个本地项目目录，在终端中启动，让它读取文件、编辑文件、运行命令、查看报错，再继续修改。

这类工具对做实证研究、数据分析、论文复现和课程项目的人很有用。原因是我们的很多任务不是开发商业软件，而是整理科研项目：

```text id="l0bfza"
project/
├─ data_raw/
├─ data_clean/
├─ code/
├─ tables/
├─ figures/
├─ logs/
└─ README.md
```

一个真实的论文复现项目，通常会遇到这些问题：

* 数据文件放在哪里；
* 脚本应该按什么顺序运行；
* 路径是不是写死在作者电脑上；
* 需要哪些 Python / R / Stata 包；
* 哪个脚本生成描述性统计；
* 哪个脚本生成主回归表；
* 哪些结果是中间文件；
* 论文中的表格和代码输出是否对应。

这些问题不是补全一行代码能解决的。它需要 AI 进入项目，连续阅读、运行、报错、修改、再运行。`Claude Code` 适合处理的正是这类任务。

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/lianxh_ai_agent_tools_fig03_repro_workflow.png)

一个更好的提示词不是：

```text id="g9cvwg"
帮我跑通这个项目。
```

而是：

```text id="p60asm"
请检查这个论文复现项目。
目标是让别人下载后可以从原始数据开始运行，
生成描述性统计、回归表和主要图形。
请先不要修改文件，先说明当前项目的问题。
```

这个提示词有两个好处。

一是目标清楚：不是随便改代码，而是让项目可复现。二是要求 AI 先诊断、后修改。这样你可以先判断它的理解是否正确，再让它继续执行。

对于本地科研项目，`Claude Code` 可以承担几类工作：

* 读懂项目目录；
* 检查依赖和运行顺序；
* 修改本地路径；
* 修复脚本报错；
* 生成运行说明；
* 整理 `README.md`；
* 为课程示例补充注释；
* 把零散脚本改成更清楚的项目结构。

不过，`Claude Code` 不是魔法。它能运行命令，也可能误运行命令；它能改文件，也可能改错文件。使用时要特别注意三件事：

* 不要把敏感数据、未公开论文、账号密钥随意交给它；
* 让它修改前先给计划；
* 每轮修改后查看 `diff` 和运行结果。

如果项目涉及 Stata、R、Python 混合脚本，还要提前说明本机环境。例如：

```text id="9qhwfx"
本项目中 Python 使用 dml050 环境，
Stata 安装在 D:/stata17，
R 使用 RStudio 和 renv。
请不要假设所有命令都可以直接运行，
先检查项目中的说明文件和脚本。
```

这类信息看似琐碎，但对 Agent 很关键。Agent 越能接触本地环境，越需要你给它清楚边界。

费用方面，`Claude Code` 的成本与订阅计划、模型选择、代码库规模和使用方式有关。Anthropic 文档中专门提供了 [Claude Code 成本管理说明](https://code.claude.com/docs/en/costs)。第一次使用时，不宜直接把大项目交给它长时间自动运行，而应先让它读目录、列计划、分步骤执行。

## 5. Codex：适合把明确代码任务交给 Agent

[Codex](https://chatgpt.com/codex/) 是 OpenAI 体系中的代码 Agent。它既可以通过 [Codex CLI](https://github.com/openai/codex) 在本地项目中工作，也可以通过 [Codex Web](https://developers.openai.com/codex/cloud)、IDE 和 GitHub 工作流处理代码任务。

和 `Claude Code` 相比，`Codex` 更像「任务代理」。如果你能把任务说清楚，它可以围绕这个任务进行修改、运行和交付。

例如：

```text id="373nra"
请为 code/clean_data.py 中的核心函数补充测试。
测试数据放在 tests/fixtures/ 中。
运行测试后，如果发现函数有问题，请修复并说明原因。
```

这个任务比「帮我写代码」清楚得多。它说明了：

* 修改对象是哪个文件；
* 测试放在哪里；
* 要先运行测试；
* 如果测试暴露问题，再修复函数；
* 最后说明原因。

这类任务很适合 `Codex`。它不只是聊天，而是围绕一个代码目标完成一块工作。

如果项目已经托管在 GitHub 上，`Codex` 的价值更明显。比如，你可以围绕 issue、pull request、测试失败、代码审查来使用它。OpenAI 文档中有专门的 [Codex GitHub code review](https://developers.openai.com/codex/integrations/github) 说明，展示了如何在 GitHub pull request 中请求 `@codex review`，以及如何让 Codex 根据 review 结果继续修复问题。

`Codex` 适合这些场景：

* 修复一个明确 bug；
* 为已有函数补测试；
* 解释一个仓库结构；
* 根据 issue 修改代码；
* 检查 pull request；
* 把任务结果整理成 diff 或说明。

如果只是刚开始学编程，`Codex` 未必是第一选择。它更适合已经有项目、有文件、有测试、有明确任务的场景。

换句话说，`Codex` 的关键不是「让 AI 自己想做什么」，而是「你能不能把任务定义清楚」。

费用和可获得性方面，可以查看 [Codex Pricing](https://chatgpt.com/codex/pricing/) 和 [Codex CLI GitHub 仓库](https://github.com/openai/codex)。需要注意的是，OpenAI 的 Codex 既和 ChatGPT 订阅体系有关，也会涉及 credits 和 token 消耗。使用前应确认自己当前账号是否包含相应权限。

## 6. 费用和可获得性：免费不等于低成本

很多人很关心费用，这很正常。但 AI 编程工具的成本不能只看月费。

现在很多工具都在采用类似下面的结构：

$$
\operatorname{Cost}=\operatorname{Subscription}+\operatorname{Credits}+\operatorname{API\ Tokens}+\operatorname{Debug\ Time}
$$

- `Subscription` 是订阅费，比如每月付费。
- `Credits` 是平台给你的使用额度。
- `API Tokens` 是按输入和输出 token 计费。
- `Debug Time` 则是最容易被忽视的成本：环境没配好、任务没说清、Agent 反复改错，都会消耗时间和额度。

所以，一个工具标价不高，并不意味着可以无限使用。一次大型项目扫描、一次长时间 Agent 自动修改、一次反复运行失败的任务，都可能快速消耗 credits。

判断费用时需要考虑一下问题：

* 有没有免费版？
* 免费版限制在哪里？
* 是否需要美元信用卡？
* 是否支持国内支付？
* 是否需要 API key？
* 额度用完后是否自动扣费？
* 能否设置预算上限？
* 是否适合办公室、实验室或课程统一配置？

需要说明的是，AI 编程工具的价格和权益变化很快。写教程时，不宜把具体价格写得过满；购买前，一定要以官网当前页面为准。

更稳妥的建议是：

* 第一次使用时，先用免费版或低档订阅；
* 不要一开始就开自动续费或自动充值；
* 不要让 Agent 长时间无人监督地运行；
* 大项目先让 AI 读目录和制定计划，不要直接改；
* API key 要设预算，不要裸奔。

AI-Agent 的成本不是「问一次多少钱」，而是「一个任务跑完整要消耗多少上下文、多少轮修改和多少次命令执行」。

## 7. 其它工具

除了上面四个工具，还有不少可选方案。国内用户可以关注：

| 工具                                                                               | 简要定位                                         |
| ---------------------------------------------------------------------------------- | ------------------------------------------------ |
| [Qoder CN](https://help.aliyun.com/zh/lingma/product-overview/billing-description) | 原通义灵码，适合国内账号、中文环境和阿里云生态   |
| [CodeBuddy](https://cloud.tencent.com/document/product/1749/126592)                | 腾讯云代码助手，适合需要中文界面和国内服务的用户 |
| [Trae](https://www.trae.ai/pricing)                                                | AI IDE 型工具，适合尝试低门槛 AI 编辑器          |

开源和进阶用户可以关注：

| 工具                                                                    | 简要定位                                                     |
| ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| [Aider](https://github.com/aider-ai/aider)                              | 命令行结对编程工具，适合熟悉 Git 和终端的用户                |
| [Cline](https://cline.bot/)                                             | VS Code 和终端中的 Agent 工具，灵活但需要理解模型和 API 配置 |
| [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/overview/) | 开源终端 Agent，适合 Qwen 系列模型和开源模型实验             |
| [OpenHands](https://www.openhands.dev/)                                 | 更偏工程化、自托管和团队任务，不适合完全新手                 |
| [Devin](https://devin.ai/)                                              | 更像云端软件工程 Agent，适合成熟项目和团队协作               |

还有一条值得单独讲的路径：调用国内大模型 API。

例如，[DeepSeek API](https://api-docs.deepseek.com/)、Qwen、Kimi、GLM 等模型都可以在一定程度上作为底层模型接入部分 Agent 工具。以 DeepSeek 为例，其文档说明 API 兼容 OpenAI / Anthropic 格式，并提供 `base_url`、`api_key`、`model` 等调用参数；其 [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing) 页面也按百万 token 说明输入和输出计费方式。

这条路径的好处是成本较低、中文环境友好、国内账号和支付更方便。问题是，使用者需要理解 `API key`、`base_url`、`model name`、token 计费和上下文长度等概念。

![](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/lianxh_ai_agent_tools_fig04_low_cost_path.png)

这已经不是「选哪个 AI 编程工具」的问题，而是「如何低成本配置自己的 Agent 工作流」的问题。

## 8. 如何选择？

最终的建议是：选择 AI 编程工具时，要根据任务类型和需求来选，而不是一味地追求最强、最贵的模型。

* **写课程作业、小脚本、小函数**：优先考虑 `GitHub Copilot`、`CodeBuddy`、`Qoder CN`。这类工具主要帮助补全代码、解释语法和处理简单报错。

* **在 VS Code 或编辑器里修改项目**：优先考虑 `Cursor`。它适合阅读已有代码、解释项目结构、修改局部脚本、整理输出目录。

* **整理本地论文复现项目**：优先考虑 `Claude Code`。它适合检查路径、读取目录、运行脚本、修复报错、整理 `README.md` 和复现说明。

* **处理明确的代码任务或 GitHub 仓库**：优先考虑 `Codex`。它适合围绕 issue、测试、PR、代码审查和明确 bug 修复展开工作。

* **想降低成本，且愿意配置模型和 API**：可以考虑 `Aider`、`Cline`、`Qwen Code` 搭配国内模型 API。这条路径更灵活，但需要理解 `API key`、`base_url`、`model name` 和 token 计费。

* **主要考虑国内账号、国内支付和中文环境**：可以优先考虑 `Qoder CN`、`CodeBuddy`、`Trae`。它们在中文界面、国内服务和支付便利性方面通常更友好。

简言之，写小脚本，用代码补全；改课程项目，用 AI IDE；整理论文复现，用终端 Agent；维护仓库和 PR，再用任务代理；想降成本，再考虑国内模型 API 和开源工具。


## 8. 参考资料

### 主要工具官网与文档

* GitHub. (2026). GitHub Copilot plans and pricing. [Link](https://github.com/features/copilot/plans), [Docs](https://docs.github.com/en/copilot/get-started/plans), [Google](https://scholar.google.com/scholar?q=GitHub+Copilot+plans+and+pricing).

* Cursor. (2026). Cursor: The AI code editor. [Link](https://cursor.com/), [Pricing](https://cursor.com/pricing), [Docs](https://docs.cursor.com/), [Google](https://scholar.google.com/scholar?q=Cursor+AI+code+editor).

* Anthropic. (2026). Claude Code overview. [Link](https://code.claude.com/docs/en/overview), [Costs](https://code.claude.com/docs/en/costs), [Google](https://scholar.google.com/scholar?q=Claude+Code+agentic+coding+tool).

* OpenAI. (2026). Codex. [Link](https://chatgpt.com/codex/), [Pricing](https://chatgpt.com/codex/pricing/), [Codex CLI](https://github.com/openai/codex), [Codex Web](https://developers.openai.com/codex/cloud), [GitHub Review](https://developers.openai.com/codex/integrations/github), [Google](https://scholar.google.com/scholar?q=OpenAI+Codex+coding+agent).

### 国内工具与低成本模型入口

* 阿里云. (2026). Qoder CN 计费说明. [Link](https://help.aliyun.com/zh/lingma/product-overview/billing-description), [Qoder](https://qoder.com/), [Google](https://scholar.google.com/scholar?q=Qoder+CN+AI+coding+assistant).

* 腾讯云. (2026). 腾讯云代码助手 CodeBuddy 计费概述. [Link](https://cloud.tencent.com/document/product/1749/126592), [CodeBuddy](https://www.codebuddy.cn/pricing/), [Google](https://scholar.google.com/scholar?q=CodeBuddy+AI+coding+assistant).

* Trae. (2026). Trae pricing. [Link](https://www.trae.ai/pricing), [Google](https://scholar.google.com/scholar?q=Trae+AI+IDE+coding+agent).

* DeepSeek. (2026). DeepSeek API documentation. [Link](https://api-docs.deepseek.com/), [Pricing](https://api-docs.deepseek.com/quick_start/pricing), [Google](https://scholar.google.com/scholar?q=DeepSeek+API+pricing+OpenAI+compatible).

### 开源和进阶 Agent 工具

* Aider. (2026). Aider: AI pair programming in your terminal. [Link](https://github.com/aider-ai/aider), [Docs](https://aider.chat/docs/), [Google](https://scholar.google.com/scholar?q=Aider+AI+pair+programming+terminal).

* Cline. (2026). Cline: The open coding agent. [Link](https://cline.bot/), [GitHub](https://github.com/cline/cline), [Google](https://scholar.google.com/scholar?q=Cline+open+source+coding+agent).

* Qwen. (2026). Qwen Code overview. [Link](https://qwenlm.github.io/qwen-code-docs/en/users/overview/), [GitHub](https://github.com/QwenLM/qwen-code), [Google](https://scholar.google.com/scholar?q=Qwen+Code+terminal+AI+coding+agent).

* OpenHands. (2026). OpenHands: The open platform for cloud coding agents. [Link](https://www.openhands.dev/), [GitHub](https://github.com/OpenHands/openhands), [Google](https://scholar.google.com/scholar?q=OpenHands+cloud+coding+agent).

* Devin. (2026). Devin: The AI software engineer. [Link](https://devin.ai/), [Google](https://scholar.google.com/scholar?q=Devin+AI+software+engineer).

### 参考文献
- Zhou, X., Liang, P., Zhang, B., Li, Z., Ahmad, A., Shahin, M., & Waseem, M. (2023). Exploring the problems, their causes and solutions of AI pair programming: A study on GitHub and Stack Overflow. arXiv. [Link](https://doi.org/10.48550/arXiv.2311.01020), [PDF](https://arxiv.org/pdf/2311.01020.pdf), [Google](<https://scholar.google.com/scholar?q=Exploring+the+problems+their+causes+and+solutions+of+AI+pair+programming+A+study+on+GitHub+and+Stack+Overflow>).

- Chatlatanagulchai, W., Thonglek, K., Reid, B., Kashiwa, Y., Leelaprute, P., Rungsawang, A., Manaskasemsak, B., & Iida, H. (2025). On the Use of Agentic Coding Manifests: An Empirical Study of Claude Code. arXiv. [Link](https://doi.org/10.48550/arXiv.2509.14744), [PDF](https://arxiv.org/pdf/2509.14744.pdf), [Google](<https://scholar.google.com/scholar?q=On+the+Use+of+Agentic+Coding+Manifests+An+Empirical+Study+of+Claude+Code>).

- Liu, J., Zhao, X., Shang, X., & Shen, Z. (2026). Dive into Claude Code: The Design Space of Today’s and Future AI Agent Systems. arXiv. [Link](https://doi.org/10.48550/arXiv.2604.14228), [PDF](https://arxiv.org/pdf/2604.14228.pdf), [Google](<https://scholar.google.com/scholar?q=Dive+into+Claude+Code+The+Design+Space+of+Today%27s+and+Future+AI+Agent+Systems>).

- Li, H., Zhang, H., & Hassan, A. E. (2026). AIDev: Studying AI Coding Agents on GitHub. arXiv. [Link](https://doi.org/10.48550/arXiv.2602.09185), [PDF](https://arxiv.org/pdf/2602.09185.pdf), [Google](<https://scholar.google.com/scholar?q=AIDev+Studying+AI+Coding+Agents+on+GitHub>).

- Wang, X., Rosenberg, S., Michelini, J., Smith, C., Tran, H., Engel, N., Malhotra, R., Zhou, X., Chen, V., Brennan, R., & Neubig, G. (2025). The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents. arXiv. [Link](https://doi.org/10.48550/arXiv.2511.03690), [PDF](https://arxiv.org/pdf/2511.03690.pdf), [Google](<https://scholar.google.com/scholar?q=The+OpenHands+Software+Agent+SDK+A+Composable+and+Extensible+Foundation+for+Production+Agents>).


## 9. 相关推文

> Note：产生如下推文列表的 Stata 命令为：   
> &emsp; `lianxh agent claude codex,md2 nocat`  
> 安装最新版 `lianxh` 命令：    
> &emsp; `ssc install lianxh, replace` 
  
  - 丁星星, 2026, [用 AI Agent 收集数据：如何保证质量和可重复性？](https://www.lianxh.cn/details/1816.html).
  - 丁闪闪, 2026, [AI我知道-01：AI 怎么读懂你的话？Token、上下文窗口与提示词](https://www.lianxh.cn/details/1770.html).
  - 丁闪闪, 2026, [AI我知道-02：AI 为什么会出错？注意力机制、幻觉与推理模型](https://www.lianxh.cn/details/1771.html).
  - 丁闪闪, 2026, [AI我知道-04：AI 如何自己干活?Agent、工具调用与 MCP](https://www.lianxh.cn/details/1774.html).
  - 林芷涵, 2026, [Claude Code Skills 写作指南：如何写好一个可复用的 SKILL.md](https://www.lianxh.cn/details/1791.html).
  - 王烨文, 2025, [LLM Agent：大语言模型的智能体图解](https://www.lianxh.cn/details/1650.html).
  - 罗丹, 2025, [提示词！提示词！数据清洗、数据分析、可视化一网打尽](https://www.lianxh.cn/details/1638.html).
  - 艾米丽, 2026, [Claude 工程师力推 HTML 取代 Markdown，你怎么看？](https://www.lianxh.cn/details/1788.html).
  - 艾米丽, 2026, [TradingAgents 爆火：AI 炒股，终于从问答走向投研团队](https://www.lianxh.cn/details/1778.html).
  - 连享会, 2026, [✨ 助教招聘-连享会 · A · 2026-AI-Agent 专题课](https://www.lianxh.cn/details/1785.html).
  - 连享会, 2026, [公开课：Claude Code 协同 Stata：环境配置与应用实践](https://www.lianxh.cn/details/1767.html).
  - 连享会, 2026, [连享会 · A · 2026-AI-Agent 专题课](https://www.lianxh.cn/details/1777.html).
  - 连小白, 2026, [OpenBB 爆火：用于投喂 AI-Agent 的开源数据平台](https://www.lianxh.cn/details/1789.html).
  - 连小白, 2026, [从 Prompt 到 Skills：把论文复现、数据清洗和代码规范写进 AI](https://www.lianxh.cn/details/1790.html).
  - 连小白, 2026, [没有 Claude Code，如何实现 Skills？ChatGPT、DeepSeek、豆包](https://www.lianxh.cn/details/1794.html).
  - 连玉君, 2026, [老连也会画画了！AI 文生图功能太强大](https://www.lianxh.cn/details/1780.html).
  - 颜国强, 2026, [从 15 分钟到 5 小时：2025 年大模型能力跃迁全景图](https://www.lianxh.cn/details/1750.html).
 
