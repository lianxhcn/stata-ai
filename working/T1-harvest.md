# T1：素材收割

## 目标

从三个本地仓库把指定源文件复制到 `_materials/harvest/`，生成清单报告。
**对源仓库只读，绝不修改。**

## 步骤

### 1. 读取仓库路径

打开 `_materials/三个仓库的本地路径.md`，获得 ci-policy、stata101、ds2026 的本地路径。
逐一确认路径存在；不存在则停下询问。

### 2. 建立输出目录

```
_materials/harvest/
├── cipolicy/
├── stata101/
├── ds2026/
└── MANIFEST.md
```

### 3. 收割清单

文件名以实际仓库为准，下列名称是模糊匹配线索（先按名找，找不到再按关键词全库搜索）。
只复制**源文件**（.qmd/.md/.ipynb/.yml/.scss/.css/.bib/图片），不要编译产物（.html）。

**A. ci-policy →`harvest/cipolicy/`**

1. `_quarto.yml`
2. `index.qmd`、`syllabus.qmd`、`settings.qmd`
3. `_quarto.yml` 中引用到的全部样式与辅助文件（theme/scss/css、include 头尾文件、
   references.bib、csl 等——逐行核对 _quarto.yml 里出现的每个文件引用）
4. `images/` 整个文件夹
5. `lectures/` 下文件名含 `ai_agent` 或 `08` 的章节源文件
6. `notebooks/` 下与 DID 相关的文件夹（文件名含 `did`）
7. `.github/workflows/` 若存在，整个复制
8. 记录：该仓库的发布方式线索（_quarto.yml 中的 output-dir 设定；是否存在 docs/ 目录）

**B. stata101 → `harvest/stata101/`**（一般在 body/ 下）

- B1（界面）、B2a（工作流程）、B2b（profile）、B3（语法格式）、
  B4（帮助文件和外部命令）、B6（do 文档）、R9（回归结果的呈现和输出）

**C. ds2026 → `harvest/ds2026/`**

- Lecture/00-setup/ 下：`01_00_coding_with_AI`、`01_02_jupyter_notebook`、`01_04_markdown`
- appendix_python/ 下：`a2_project`、`a3_concepts`、`a8_workflow`
- **全库搜索关键词 `nbstata`**（不区分大小写），把命中的源文件全部复制到
  `harvest/ds2026/nbstata_hits/`，并在 MANIFEST 中单独列出。settings 页的 nbstata
  一节依赖这个搜索结果；若全库无命中，明确写入 MANIFEST。

### 4. 生成 MANIFEST.md

逐仓库列表：目标文件 → 实际找到的路径 → 是否复制成功 → 文件大小。
末尾三节：①未找到清单；②nbstata 搜索结果；③ci-policy 发布方式结论。

## 完成标准

- harvest/ 三个子目录齐全，MANIFEST.md 可读；
- 向人汇报：找到 X 件、缺 Y 件（列名）、nbstata 结论、发布方式结论；
- **停止，等待确认后再进入 T2。**
