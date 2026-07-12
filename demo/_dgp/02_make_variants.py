# -*- coding: utf-8 -*-
"""
02_make_variants.py —— 在 01_gen_data.do 生成的数据基础上做两件事：
  1) 给主 demo（demo/01_data）的 city_economic 增加一列文字分类变量 region（东/中/西部），
     作为"文字变量需转数字 + 建对应表"的清洗演示点；
  2) 生成一份"更脏"的练习数据 demo/01_data_messy/，在标准瑕疵之外再埋入：
     离群值、非标准缺失标记、数字被存成文本（带千分位逗号）等，供学员练手/老师测试提示词。

约束：只在"观测层"加噪，不改底层 y/tau，dgp_truth.md 的真值对两份数据都成立。
埋点答案清单写到 working/（不发布）。可复现：随机放置用固定 seed。
运行：python demo/_dgp/02_make_variants.py   （在仓库根目录）
"""
import csv, os, random

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D_CLEAN = os.path.join(ROOT, "demo", "01_data")
D_MESSY = os.path.join(ROOT, "demo", "01_data_messy")
WORKING = os.path.join(ROOT, "working")
random.seed(20260712)

# ---------- 城市 → 区域（东/中/西部）映射 ----------
EAST = ("南京 无锡 徐州 常州 苏州 南通 连云港 淮安 盐城 扬州 镇江 泰州 宿迁 "
        "杭州 宁波 温州 嘉兴 湖州 绍兴 金华 衢州 舟山 台州 丽水 "
        "福州 厦门 莆田 三明 泉州 漳州 南平 龙岩 宁德 "
        "济南 青岛 淄博 枣庄 东营 烟台 潍坊 济宁 泰安 威海 日照 临沂 德州 菏泽 "
        "广州 深圳 珠海 汕头 佛山 韶关 湛江 肇庆 江门 茂名 惠州 中山").split()
CENTRAL = ("合肥 芜湖 蚌埠 淮南 马鞍山 安庆 滁州 阜阳 宿州 六安 "
           "南昌 九江 赣州 吉安 宜春 上饶 抚州 景德镇 "
           "郑州 开封 洛阳 平顶山 安阳 新乡 焦作 许昌 漯河 南阳 商丘 信阳 "
           "武汉 黄石 十堰 宜昌 襄阳 荆门 孝感 荆州 黄冈 咸宁 "
           "长沙 株洲 湘潭 衡阳 邵阳 岳阳 常德 郴州 永州 怀化").split()
WEST = ("成都 自贡 泸州 德阳 绵阳 乐山 南充 宜宾 西安 兰州 贵阳").split()
REGION = {}
for c in EAST: REGION[c] = "东部"
for c in CENTRAL: REGION[c] = "中部"
for c in WEST: REGION[c] = "西部"

def read_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.reader(f))

def write_csv(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)

# ==========================================================
# 1) 主 demo：给 city_economic 增加 region 列
# ==========================================================
econ = read_csv(os.path.join(D_CLEAN, "city_economic.csv"))
h = econ[0]; iname = h.index("city_name")
if "region" not in h:
    econ[0] = h + ["region"]
    for r in econ[1:]:
        r.append(REGION.get(r[iname], "西部"))
write_csv(os.path.join(D_CLEAN, "city_economic.csv"), econ)
print("主 demo city_economic 已加 region 列")

# ==========================================================
# 2) 生成脏版 demo/01_data_messy/
# ==========================================================
log = []  # 埋点答案清单

# --- economic（脏）：region + gdp 存成文本(千分位) + 少量离群/非标准缺失 ---
me = [list(r) for r in econ]                       # 已含 region
h = me[0]; ig, ip, iss = h.index("gdp"), h.index("pop"), h.index("second_share")
# (a) gdp 全列存成带千分位逗号的文本
for r in me[1:]:
    try: r[ig] = f"{float(r[ig]):,.1f}"
    except ValueError: pass
log.append("economic.gdp：整列被存成带千分位逗号的文本（如 21,736.9），导入后是字符串，需去逗号转数值。")
# (b) gdp 2 个明显错误值
body = me[1:]
for k in random.sample(range(len(body)), 2):
    body[k][ig] = random.choice(["0", "-1"])
log.append("economic.gdp：2 处明显错误值（0 或 -1）。")
# (c) pop 2 个离群值
for k in random.sample(range(len(body)), 2):
    body[k][ip] = "99999"
log.append("economic.pop：2 处离群值 99999（万人，明显不合理）。")
# (d) second_share ~2% 非标准缺失标记
n_ss = max(3, int(len(body) * 0.02))
for k in random.sample(range(len(body)), n_ss):
    body[k][iss] = random.choice(["", "NA", "-"])
log.append(f"economic.second_share：{n_ss} 处非标准缺失标记（空 / NA / -）。")
write_csv(os.path.join(D_MESSY, "city_economic.csv"), me)

# --- green（脏）：继承标准瑕疵 + 离群值 + 非标准缺失 ---
green = read_csv(os.path.join(D_CLEAN, "city_green.csv"))
hg = green[0]; igp = hg.index("green_patents")
gbody = green[1:]
# (a) 3 个离群值：×100 录入错误
out_idx = random.sample(range(len(gbody)), 3)
for k in out_idx:
    try: gbody[k][igp] = f"{float(gbody[k][igp]) * 100:.1f}"
    except ValueError: pass
log.append("green.green_patents：3 处离群值（原值 ×100 的录入错误）。")
# (b) ~2% 非标准缺失标记
n_g = max(3, int(len(gbody) * 0.02))
for k in random.sample(range(len(gbody)), n_g):
    gbody[k][igp] = random.choice(["", "NA", ".", "-"])
log.append(f"green.green_patents：{n_g} 处非标准缺失标记（空 / NA / . / -）。")
write_csv(os.path.join(D_MESSY, "city_green.csv"), green)

# --- policy（脏）：与主 demo 相同（保留"市"后缀不一致），原样复制 ---
policy = read_csv(os.path.join(D_CLEAN, "policy_pilot.csv"))
write_csv(os.path.join(D_MESSY, "policy_pilot.csv"), policy)

print("脏版已写入 demo/01_data_messy/")

# ==========================================================
# 3) 埋点答案清单 → working/（不发布）
# ==========================================================
ans = ["# demo/01_data_messy/ 埋点答案清单（不发布，供老师核对 Agent 的查验结果）",
       "",
       "> 由 demo/_dgp/02_make_variants.py 生成（seed=20260712）。真值不变，见 dgp_truth.md。",
       "",
       "## 继承自主 demo 的标准瑕疵",
       "- green：2015 及以前「淮安→淮阴」「襄阳→襄樊」（旧称）；随机缺失约 3% 行；末尾 12 行重复。",
       "- policy：约一半城市名带「市」后缀，与 economic 的规范名不一致。",
       "- 三表主键口径不一，需用 economic 作桥（city_name ↔ city_code）。",
       "",
       "## 脏版额外埋入"]
ans += [f"- {x}" for x in log]
ans += ["", "## 期望 Agent 在「查验清洗」阶段报告出来的问题",
        "字段类型（gdp 是文本）、离群值、非标准缺失标记、重复行、跨表城市名不一致（改名/后缀）、"
        "以及 region 这一文字分类变量需要编码为数字并建立对应表。"]
with open(os.path.join(WORKING, "01_data_messy_埋点答案.md"), "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(ans) + "\n")
print("埋点答案清单已写入 working/01_data_messy_埋点答案.md")
print("done")
