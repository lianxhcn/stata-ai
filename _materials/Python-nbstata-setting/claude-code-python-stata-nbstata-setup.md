# 给 Claude Code 的本机 Python、Stata 与 nbstata 配置说明

本文档用于让 Claude Code 在本机正确识别 Python 环境、Stata 可执行文件，以及 Jupyter 中使用的 `nbstata` 插件。请优先按本文档中的路径和命令执行，不要自行猜测 Python、Conda 或 Stata 的安装位置。

`retrieved_date`: 2026-07-10

## 1. 本机已确认的环境信息

当前机器是 Windows 环境，主要使用 PowerShell。

已确认路径如下：

```powershell
$env:PYTHON_EXE      = "C:\Users\Administrator\.conda\envs\dml050\python.exe"
$env:CONDA_EXE       = "C:\ProgramData\anaconda3\Scripts\conda.exe"
$env:PYTHON_ENV_NAME = "dml050"
$env:STATA_EXE       = "D:\stata19\StataMP-64.exe"
$env:RSCRIPT_EXE     = "C:\Program Files\R\R-4.4.3\bin\Rscript.exe"
```

已确认版本：

```text
Python 3.11.14
Conda environments:
  base   C:\ProgramData\anaconda3
  dml050 C:\Users\Administrator\.conda\envs\dml050
Stata executable:
  D:\stata19\StataMP-64.exe
```

Claude Code 在执行本地代码前，应先运行以下检查命令：

```powershell
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [System.Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = "utf-8"

Test-Path $env:PYTHON_EXE
Test-Path $env:CONDA_EXE
Test-Path $env:STATA_EXE
Test-Path $env:RSCRIPT_EXE

& $env:PYTHON_EXE --version
& $env:CONDA_EXE info --envs
```

如果 Claude Code 的 shell 会话中没有这些环境变量，可以在当前 PowerShell 会话里临时设置：

```powershell
$env:PYTHON_EXE      = "C:\Users\Administrator\.conda\envs\dml050\python.exe"
$env:CONDA_EXE       = "C:\ProgramData\anaconda3\Scripts\conda.exe"
$env:PYTHON_ENV_NAME = "dml050"
$env:STATA_EXE       = "D:\stata19\StataMP-64.exe"
$env:RSCRIPT_EXE     = "C:\Program Files\R\R-4.4.3\bin\Rscript.exe"
```

不要修改系统级 `PATH`、注册表、全局 Stata 配置或全局 Python 配置，除非用户明确授权。

## 2. Python 的使用规则

默认 Python 环境是 Conda 环境 `dml050`：

```powershell
C:\Users\Administrator\.conda\envs\dml050\python.exe
```

执行 Python 脚本时，优先使用：

```powershell
& $env:PYTHON_EXE "code\main.py"
```

如果项目根目录存在 `.venv`，优先使用项目自己的虚拟环境：

```powershell
.\.venv\Scripts\python.exe "code\main.py"
```

如果需要显式通过 Conda 环境名运行：

```powershell
& $env:CONDA_EXE run -n $env:PYTHON_ENV_NAME python "code\main.py"
```

安装 Python 包时，优先安装到 `dml050` 环境：

```powershell
& $env:PYTHON_EXE -m pip install 包名
```

不要直接运行裸命令 `python` 或 `pip`，因为 Claude Code 可能会找到错误的 Python。

## 3. Stata 的使用规则

本机 Stata 版本为 Stata 19 MP，可执行文件路径为：

```text
D:\stata19\StataMP-64.exe
```

运行 `.do` 文件时使用：

```powershell
& $env:STATA_EXE /e do "code\main.do"
```

运行后应检查对应的 `.log` 文件，确认没有 `r(...)` 错误。

如果只是测试 Stata 是否可执行，可以创建一个最小 do-file，例如：

```stata
clear all
set more off
sysuse auto, clear
summarize price mpg
display "Stata smoke test OK"
exit, clear
```

然后运行：

```powershell
& $env:STATA_EXE /e do "tmp\stata_smoke_test.do"
```

不要把 Stata 路径写死到项目脚本里。项目脚本中如需调用 Stata，应读取 `$env:STATA_EXE`。

## 4. nbstata 的作用

`nbstata` 是一个 Jupyter kernel，用来在 Jupyter Notebook、JupyterLab、VS Code Notebook 或 Quarto 中直接运行 Stata 代码。它基于 Stata 官方的 `pystata` 机制，因此要求本机已经安装并授权 Stata 17 或更高版本。

当前本机满足版本要求：已安装 Stata 19 MP，Python 为 3.11.14。

需要注意：我在 2026-07-10 检查时，`dml050` 环境中尚未检测到 `nbstata`：

```text
WARNING: Package(s) not found: nbstata
ModuleNotFoundError: No module named 'nbstata'
```

因此 Claude Code 如果需要执行 Stata notebook 或 Quarto 中的 Stata chunk，应先安装并配置 `nbstata`。

官方信息：

- PyPI: <https://pypi.org/project/nbstata/>
- User Guide: <https://hugetim.github.io/nbstata/user_guide.html>

截至 2026-07-10，PyPI 显示 `nbstata` 最新版本为 `0.8.6`，发布日期为 2026-01-22；官方说明要求 Python 3.10+，并说明 `nbstata` 适用于 Stata 17+。

## 5. 安装 nbstata

在 PowerShell 中运行：

```powershell
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [System.Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = "utf-8"

$env:PYTHON_EXE      = "C:\Users\Administrator\.conda\envs\dml050\python.exe"
$env:CONDA_EXE       = "C:\ProgramData\anaconda3\Scripts\conda.exe"
$env:PYTHON_ENV_NAME = "dml050"
$env:STATA_EXE       = "D:\stata19\StataMP-64.exe"

& $env:PYTHON_EXE -m pip install --upgrade pip
& $env:PYTHON_EXE -m pip install nbstata
& $env:PYTHON_EXE -m nbstata.install --sys-prefix --conf-file
```

说明：

- `pip install nbstata` 安装 Python 包。
- `python -m nbstata.install --sys-prefix --conf-file` 把 Stata kernel 安装到当前 Conda 环境，并生成配置文件。
- `--sys-prefix` 表示将 kernel 安装到 `dml050` 环境内部。
- `--conf-file` 表示生成 `nbstata.conf` 配置文件。

安装完成后，检查：

```powershell
& $env:PYTHON_EXE -m pip show nbstata
& $env:PYTHON_EXE -c "import nbstata; print(nbstata.__file__)"
& $env:PYTHON_EXE -m jupyter kernelspec list
```

如果 `jupyter` 命令不可用，可以先安装 JupyterLab：

```powershell
& $env:PYTHON_EXE -m pip install jupyterlab
```

## 6. nbstata 配置文件

`nbstata` 官方文档说明，配置文件可能位于以下位置：

- 使用 `--sys-prefix` 时：`[sys.prefix]\etc\nbstata.conf`
- 未使用 `--sys-prefix` 时：`~\.config\nbstata\nbstata.conf`
- 若两个位置都存在，用户主目录下的配置优先。

本机建议优先使用当前 Conda 环境内的配置文件：

```text
C:\Users\Administrator\.conda\envs\dml050\etc\nbstata.conf
```

配置文件内容建议如下：

```ini
[nbstata]
stata_dir = D:\stata19
edition = mp
splash = False
graph_format = png
graph_width = default
graph_height = default
echo = False
browse_auto_height = False
```

解释：

- `stata_dir = D:\stata19` 指向 Stata 安装目录，不是 `StataMP-64.exe` 文件本身。
- `edition = mp` 对应 Stata MP。
- `splash = False` 避免 notebook 启动时输出过多启动信息。
- `graph_format = png` 适合在 Jupyter、VS Code、Word 和 PowerPoint 中显示和复制。
- `echo = False` 对 Stata 18.5+ 和 Stata 19 更合适，可以减少重复回显。
- `browse_auto_height = False` 在 VS Code Notebook 中通常更稳。

如果配置文件不存在，可以由 Claude Code 创建该文件。注意只能写入当前 Conda 环境或用户配置目录，不要修改 Stata 安装目录。

## 7. 在 Jupyter 或 VS Code 中验证 nbstata

启动 JupyterLab：

```powershell
& $env:PYTHON_EXE -m jupyter lab
```

或者在项目目录启动：

```powershell
& $env:PYTHON_EXE -m jupyter lab --notebook-dir "<你的-notebook-项目目录>"
```

新建 notebook 时选择 `Stata` 或 `nbstata` kernel。

在第一个 Stata cell 中运行：

```stata
about
display c(stata_version)
display c(born_date)
sysuse auto, clear
summarize price mpg
```

再运行 nbstata magic 检查配置：

```stata
%status
```

如果 `%status` 显示的 `stata_dir` 不是 `D:\stata19`，说明配置文件没有被正确读取。此时需要检查是否存在用户主目录版本的 `nbstata.conf`，因为用户主目录版本会覆盖 Conda 环境内的配置。

## 8. 在 Quarto 中使用 nbstata

如果需要在 `.qmd` 文件中运行 Stata chunk，YAML 可以写：

```yaml
---
title: "Stata notebook example"
jupyter: nbstata
format: html
---
```

Stata chunk 示例：

````markdown
```{stata}
sysuse auto, clear
regress price mpg weight
```
````

如果 Quarto 找不到 `nbstata` kernel，先检查：

```powershell
& $env:PYTHON_EXE -m jupyter kernelspec list
```

必要时重新安装 kernel：

```powershell
& $env:PYTHON_EXE -m nbstata.install --sys-prefix --conf-file
```

## 9. 常见问题与处理

### 9.1 Claude Code 找不到 Python

不要使用裸命令：

```powershell
python --version
pip list
```

应使用：

```powershell
& $env:PYTHON_EXE --version
& $env:PYTHON_EXE -m pip list
```

如果 `$env:PYTHON_EXE` 为空，先在当前会话设置：

```powershell
$env:PYTHON_EXE = "C:\Users\Administrator\.conda\envs\dml050\python.exe"
```

### 9.2 Claude Code 找不到 Stata

先检查：

```powershell
Test-Path "D:\stata19\StataMP-64.exe"
```

如果返回 `True`，设置：

```powershell
$env:STATA_EXE = "D:\stata19\StataMP-64.exe"
```

运行 `.do` 文件时使用：

```powershell
& $env:STATA_EXE /e do "path\to\file.do"
```

### 9.3 nbstata 找不到 Stata

检查 `nbstata.conf`：

```powershell
Get-Content "C:\Users\Administrator\.conda\envs\dml050\etc\nbstata.conf" -Encoding utf8
```

确认其中包含：

```ini
[nbstata]
stata_dir = D:\stata19
edition = mp
```

如果 `%status` 显示读取的是用户目录下的配置文件，则应同步修改那个配置文件，或删除错误配置。删除配置文件前必须征得用户同意。

### 9.4 Jupyter kernelspec 中没有 nbstata

重新安装 kernel：

```powershell
& $env:PYTHON_EXE -m nbstata.install --sys-prefix --conf-file
& $env:PYTHON_EXE -m jupyter kernelspec list
```

### 9.5 notebook 里图形不显示

配置中优先使用：

```ini
graph_format = png
```

在 Stata cell 中测试：

```stata
sysuse auto, clear
scatter price mpg
```

### 9.6 中文路径或中文输出乱码

PowerShell 运行前设置 UTF-8：

```powershell
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [System.Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = "utf-8"
```

读取 Markdown、CSV、log 文件时显式指定 UTF-8：

```powershell
Get-Content "logs\quality_report.md" -Encoding utf8
```

## 10. Claude Code 执行任务时的建议顺序

1. **Step 1**: 先设置 UTF-8，并检查 `$env:PYTHON_EXE`、`$env:CONDA_EXE`、`$env:STATA_EXE` 是否存在。
2. **Step 2**: 使用 `& $env:PYTHON_EXE --version` 确认 Python 是 `dml050` 中的 Python 3.11.14。
3. **Step 3**: 使用 `Test-Path $env:STATA_EXE` 确认 Stata 19 MP 可执行文件存在。
4. **Step 4**: 如果任务需要 notebook 或 Quarto 中运行 Stata，检查并安装 `nbstata`。
5. **Step 5**: 写入或检查 `C:\Users\Administrator\.conda\envs\dml050\etc\nbstata.conf`。
6. **Step 6**: 运行 Stata smoke test：`sysuse auto, clear` 和 `summarize price mpg`。
7. **Step 7**: 如果涉及项目复现，先运行最小示例，再运行完整脚本。
8. **Step 8**: 运行结束后检查 `.log` 文件，确认没有 `r(...)` 错误。

## 11. 不要做的事情

Claude Code 不应执行以下操作：

- 不要猜测 Python、Conda 或 Stata 路径。
- 不要直接使用裸命令 `python`、`pip` 或 `stata`。
- 不要修改系统级 `PATH`。
- 不要修改注册表。
- 不要读取或写入任何密钥、token 或账户凭据。
- 不要改写 Stata 安装目录下的文件。
- 不要删除已有配置文件，除非用户明确同意。
- 不要把本机绝对路径写入可复现项目脚本；项目内部应优先使用相对路径或环境变量。

## 12. 最小可复制命令块

如果 Claude Code 只需要快速配置当前 shell，可直接复制运行：

```powershell
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
$OutputEncoding = [System.Text.UTF8Encoding]::new()
$env:PYTHONIOENCODING = "utf-8"

$env:PYTHON_EXE      = "C:\Users\Administrator\.conda\envs\dml050\python.exe"
$env:CONDA_EXE       = "C:\ProgramData\anaconda3\Scripts\conda.exe"
$env:PYTHON_ENV_NAME = "dml050"
$env:STATA_EXE       = "D:\stata19\StataMP-64.exe"
$env:RSCRIPT_EXE     = "C:\Program Files\R\R-4.4.3\bin\Rscript.exe"

Test-Path $env:PYTHON_EXE
Test-Path $env:CONDA_EXE
Test-Path $env:STATA_EXE
& $env:PYTHON_EXE --version
& $env:CONDA_EXE info --envs
```

如果需要安装并配置 `nbstata`，继续运行：

```powershell
& $env:PYTHON_EXE -m pip install --upgrade pip
& $env:PYTHON_EXE -m pip install nbstata jupyterlab
& $env:PYTHON_EXE -m nbstata.install --sys-prefix --conf-file
& $env:PYTHON_EXE -m jupyter kernelspec list
```

然后确认配置文件：

```ini
[nbstata]
stata_dir = D:\stata19
edition = mp
splash = False
graph_format = png
graph_width = default
graph_height = default
echo = False
browse_auto_height = False
```

