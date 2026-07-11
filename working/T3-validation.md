# T3 数据验证记录

- 生成时间：2026-07-11
- 生成脚本：`demo/_dgp/01_gen_data.do`（seed = 20260712，Stata 19.5 批处理）
- 真值：`working/dgp_truth.md`；生成日志：`working/dgp_build.log`
- 结论：**全部通过**，三个 CSV 合计约 104 KB（< 1 MB）。

## 1. 行数与列名

| 文件 | 数据行数 | 期望 | 列名 | 结果 |
|------|---------|------|------|:----:|
| policy_pilot.csv | 60 | 60（仅试点） | city_name, batch, pilot_year | ✅ |
| city_economic.csv | 1560 | 120×13 完整面板 | city_code, city_name, year, gdp, pop, second_share | ✅ |
| city_green.csv | 1531 | ≈1560×0.97 + 12 ≈ 1525 | city_name, year, green_patents | ✅ |

## 2. policy_pilot

- 三批各 20：batch 1/2/3 = 20/20/20 ✅
- 带「市」后缀：36/60（规格要求「约一半」，随机结果落在合理区间）✅

## 3. city_economic（完整干净面板）

- 城市数 = 120，年份 = 2012…2024（13 年）✅
- 无空字段（0 个缺失）✅

## 4. city_green（埋入三类瑕疵）

- **瑕疵①改名**：「淮阴」「襄樊」仅出现在 2012–2015；「淮安」「襄阳」仅出现在 2016–2024 ✅
- **瑕疵②缺失**：随机删除约 2.6%（41/1560）行，接近规格的 3% ✅
- **瑕疵③重复**：文件末尾追加 12 行重复（`uniq -d` 检出 12 组）✅

## 5. name–code 桥接

- 用 city_economic 的 name 作为钥匙，policy_pilot 的 60 个城市（去掉「市」后缀后）
  **全部**能匹配到规范名 → 可桥接到 city_code ✅（未匹配数 = 0）

## 6. 真值摘要（详见 dgp_truth.md，经手工复核一致）

- 整体 ATT = 2.2762（处理后单元 420 个）
- 分批 ATT：批1 = 3.30，批2 = 1.90，批3 = 0.96
- 分事件期 ATT：e=0 为 1.03，逐期放大至 e=8 的 5.10
- 设计意图：动态且分批异质的处理效应，预期 TWFE 出偏、csdid/jwdid 接近真值

## 7. 防偷看处理

- DGP 运行日志 `01_gen_data.log`（含真值计算）已移出 demo/，改存 `working/dgp_build.log`；
- 真值文件 `dgp_truth.md` 存于 `working/`（已被 `.gitignore` 忽略，不发布、不入 demo/）；
- `demo/README.md` 仅含中性提示，未泄露任何真值或瑕疵的具体位置。
