# T3：demo 演示项目搭建

## 目标

按规格生成模拟数据与任务说明书，搭好 demo/ 项目。**本任务只造数据和 README，
不做任何分析**——分析是 T4 彩排（也是课堂直播）的内容。

## 前置输入

- `working/specs/dgp-spec.md`（数据生成规格，逐条执行）
- `working/specs/demo-README-draft.md`（README 初稿，落地时微调）

## 目标结构

```
demo/
├── README.md            # 任务说明书（给"分析者 agent"读）
├── _dgp/                # 数据生成代码（下划线开头：不参与 render；分析者不得读取）
│   ├── 01_gen_data.do
│   └── check_packages.do
├── 01_data/
│   ├── policy_pilot.csv
│   ├── city_economic.csv
│   └── city_green.csv
├── 02_code/             # 空，T4 时由分析者创建
├── 03_output/           # 空
├── 04_report/           # 空
└── logs/                # 空
```

空目录放一个 `.gitkeep` 以便入库。

## 步骤

### 1. 定位 Stata

在 `C:\Program Files\` 搜索 Stata 可执行文件（StataMP-64.exe / StataSE-64.exe 等），
记下完整路径。找不到就停下询问。

### 2. 写 `_dgp/01_gen_data.do`

严格按 `dgp-spec.md` 实现。要求：

- `set seed 20260712`，全程可复现；
- 城市名单用规格附带的列表；
- 生成三个 CSV 到 `01_data/`（UTF-8 编码导出，`export delimited ..., replace`）；
- 数据瑕疵（改名、重复行、缺失、"市"后缀不一致）必须按规格数量埋入；
- 脚本最后计算真值（整体 ATT、分批 ATT、分事件期 ATT）并导出到
  `working/dgp_truth.md`（注意：写到 working/，**不放进 demo/**）。

### 3. 写 `_dgp/check_packages.do`

内容：逐条 `which reghdfe`、`which ftools`、`which csdid`、`which drdid`、
`which estout`、`which jwdid`，任何缺失则打印对应的 `ssc install` 命令。
（T4 前由人运行。）

### 4. 批处理运行

`"<Stata路径>" /e do _dgp/01_gen_data.do`（工作目录 = demo/）。
检查 .log 无 error。若 Stata 调用反复失败，允许退路：用 Python（pandas/numpy）
按同一规格与种子逻辑生成 CSV，但 01_gen_data.do 仍保留在 `_dgp/` 作为对外口径，
并在汇报中说明。

### 5. 数据验证（写入 `working/T3-validation.md`）

- 三个 CSV 的行数、列名与规格一致；
- policy_pilot：60 个试点城市、三批各 20；带"市"后缀者约占一半；
- city_economic：城市数 × 年份数 = 完整面板，无缺失；
- city_green：存在改名城市（按规格）、重复行数、缺失比例与规格相符；
- 试点城市名可通过 city_economic 的 name–code 桥接全部匹配上（清洗后）。

### 6. 写 `demo/README.md`

以 `specs/demo-README-draft.md` 为底稿，把其中占位符（城市数、年份区间等）
替换为实际值。**README 中不得出现任何真值信息或瑕疵的具体位置**
（只保留"数据可能存在质量问题，请先查验"这类中性提示）。

## 完成标准

- demo/ 结构齐全，CSV 通过验证，dgp_truth.md 在 working/ 就位；
- 汇报验证结果摘要；
- **停止。T4 由人主导启动。**
