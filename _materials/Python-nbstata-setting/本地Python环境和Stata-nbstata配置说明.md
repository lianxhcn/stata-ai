# 本机 Python / Stata / nbstata 环境说明

你当前是在我的 Windows 本机项目中工作。现在的问题不是没有 Stata，也不是没有 Python，而是你没有正确找到我本机已有的 Python 环境、Stata 执行路径和 `nbstata` 配置。请不要重新猜测路径，也不要随意全局重装环境。请按下面信息进行诊断、绑定和验证。

## 1. 已知本机环境

我的系统是 Windows。

我本机主要使用的 Python 环境如下：

* Python 发行版：Anaconda
* Python 版本：3.12.7
* `uv` 版本：0.7.8
* 常用虚拟环境名称：`dml050`

我本机主要使用的 Stata 环境如下：

* 主用版本：Stata 19 / Stata 19.5
* Stata edition：Stata/MP
* Stata 主执行文件路径：

```powershell
D:\stata19\StataMP-64.exe
```

* Stata 安装目录：

```powershell
D:\stata19
```

我也有 Stata 17 正版，但本项目应优先使用 Stata 19。除非 Stata 19 明确无法调用，不要切换到 Stata 17。

我本机已经配置并使用过 `nbstata`。当前要做的是让你在本项目中正确找到并使用它，而不是重新搭建一套彼此脱节的环境。

## 2. 工作目标

请完成以下目标：

* 找到并激活本机已有的 `dml050` Python 环境；
* 确认该环境能找到 `nbstata`、`jupyter` 和相关 kernel；
* 确认 Python 能通过 `pystata` / `stata_setup` 正确调用 Stata 19；
* 确认 `nbstata` 的配置文件中指向的是 `D:\stata19` 和 `mp`；
* 在项目中留下可复用的环境检测脚本，便于后续 agent 继续工作；
* 不要修改原始数据，不要在没有确认的情况下删除已有配置文件。

## 3. 先运行环境诊断

请在 PowerShell 中从项目根目录运行以下命令，并把输出写入 `logs/env_check.md`。如果没有 `logs/` 文件夹，请先创建。

```powershell
mkdir logs -Force

where python
where conda
where uv
where jupyter

conda env list

conda run -n dml050 python --version
conda run -n dml050 python -c "import sys; print(sys.executable)"
conda run -n dml050 python -m pip show nbstata
conda run -n dml050 python -m pip show jupyterlab
conda run -n dml050 jupyter kernelspec list

Test-Path "D:\stata19\StataMP-64.exe"
Test-Path "D:\stata19"
```

如果 `conda run -n dml050 ...` 可以正常执行，就优先使用这种方式，不要依赖交互式 shell 是否成功 `conda activate dml050`。

## 4. 建立项目级路径记录

请在项目中创建或更新下面这个文件：

```text
env/local_paths.ps1
```

内容如下：

```powershell
# 本文件记录本机环境路径，供 Claude Code / Codex / VS Code 任务复用
# 不要提交到公开仓库；如需提交，请先确认不含隐私路径或凭据信息

$env:CONDA_ENV_NAME = "dml050"

$env:STATA_DIR = "D:\stata19"
$env:STATA_EXE = "D:\stata19\StataMP-64.exe"
$env:STATA_EDITION = "mp"

$env:PYTHON_ENV_NOTE = "Use conda run -n dml050 python ..."
```

如果项目中有 `.gitignore`，请确认包含：

```gitignore
env/local_paths.ps1
```

如果没有 `.gitignore`，请新建并加入这一行。

## 5. 验证 Python 调用 Stata

请创建文件：

```text
tools/check_pystata.py
```

内容如下：

```python
# -*- coding: utf-8 -*-
"""
检查 Python 是否能通过 Stata 官方 pystata 接口调用 Stata 19。

本机 Stata 安装目录：
    D:\\stata19

本机 Stata edition：
    mp
"""

import sys
from pathlib import Path

STATA_DIR = Path(r"D:\stata19")

print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Stata dir exists:", STATA_DIR.exists())

try:
    import stata_setup
except Exception as exc:
    print("ERROR: cannot import stata_setup")
    print(repr(exc))
    raise

# splash=False 用于减少输出噪音
stata_setup.config(str(STATA_DIR), "mp", splash=False)

from pystata import stata

stata.run("display c(version)")
stata.run("display c(stata_version)")
stata.run("display c(edition)")
stata.run("sysuse auto, clear")
stata.run("summarize price mpg")
```

然后运行：

```powershell
conda run -n dml050 python tools/check_pystata.py
```

如果报错提示找不到 `stata_setup`，请优先在 `dml050` 环境内安装或升级它：

```powershell
conda run -n dml050 python -m pip install --upgrade stata_setup
```

安装后重新运行：

```powershell
conda run -n dml050 python tools/check_pystata.py
```

不要在 base 环境中安装，除非明确说明 `dml050` 不存在或不可用。

## 6. 检查并修正 nbstata 配置

`nbstata` 应指向 Stata 安装目录，而不是 Stata 可执行文件本身。我的 Stata 安装目录是：

```text
D:\stata19
```

edition 应设为：

```text
mp
```

请检查这些位置是否存在 `nbstata` 配置文件：

```powershell
$HOME\.config\nbstata\nbstata.conf
$HOME\.nbstata.conf
```

也请检查 `dml050` 环境内是否有 sys-prefix 配置。可先运行：

```powershell
conda run -n dml050 python -c "import sys; print(sys.prefix)"
```

如果需要修正配置，请优先创建或更新：

```text
%USERPROFILE%\.config\nbstata\nbstata.conf
```

内容建议如下：

```ini
[nbstata]
stata_dir = D:\stata19
edition = mp
splash = False
graph_format = png
graph_width = default
graph_height = default
echo = None
browse_auto_height = False
```

然后运行：

```powershell
conda run -n dml050 python -m nbstata.install --sys-prefix --conf-file
conda run -n dml050 jupyter kernelspec list
```

如果安装脚本重新生成配置文件，请确认最终生效的配置仍然是：

```ini
stata_dir = D:\stata19
edition = mp
```

## 7. 建立 Stata 批处理测试脚本

请创建文件：

```text
scripts/stata/00_env_test.do
```

内容如下：

```stata
/********************************************************************
  文件名：00_env_test.do
  功能：测试 Claude Code 是否能在本机调用 Stata 19 执行 do 文件
  输入：Stata 自带 auto.dta
  输出：logs/stata_env_test.log
********************************************************************/

clear all
set more off

capture log close _all
log using "logs/stata_env_test.log", replace text

display "Stata version: " c(stata_version)
display "Stata edition: " c(edition)
display "Current directory: " c(pwd)

sysuse auto, clear
summarize price mpg weight
reg price mpg weight

log close
exit
```

然后尝试通过 Stata 19 执行：

```powershell
& "D:\stata19\StataMP-64.exe" /e do "scripts\stata\00_env_test.do"
```

如果 `/e do` 在当前机器上不能正常退出或不能生成日志，请再尝试：

```powershell
& "D:\stata19\StataMP-64.exe" /b do "scripts\stata\00_env_test.do"
```

执行后检查：

```powershell
Test-Path "logs\stata_env_test.log"
Get-Content "logs\stata_env_test.log" -TotalCount 80
```

## 8. 建立统一的一键检测脚本

请创建文件：

```text
tools/check_local_env.ps1
```

内容如下：

```powershell
# 本脚本用于检查本项目能否找到 Python、nbstata 和 Stata 19

$ErrorActionPreference = "Continue"

Write-Host "=== Basic paths ==="
where python
where conda
where uv
where jupyter

Write-Host "`n=== Conda envs ==="
conda env list

Write-Host "`n=== Python in dml050 ==="
conda run -n dml050 python --version
conda run -n dml050 python -c "import sys; print(sys.executable)"

Write-Host "`n=== Python packages ==="
conda run -n dml050 python -m pip show nbstata
conda run -n dml050 python -m pip show stata_setup
conda run -n dml050 python -m pip show jupyterlab

Write-Host "`n=== Jupyter kernels ==="
conda run -n dml050 jupyter kernelspec list

Write-Host "`n=== Stata path ==="
Test-Path "D:\stata19\StataMP-64.exe"
Test-Path "D:\stata19"

Write-Host "`n=== pystata test ==="
conda run -n dml050 python tools/check_pystata.py

Write-Host "`n=== Stata do-file test ==="
& "D:\stata19\StataMP-64.exe" /e do "scripts\stata\00_env_test.do"

Write-Host "`n=== Stata log preview ==="
if (Test-Path "logs\stata_env_test.log") {
    Get-Content "logs\stata_env_test.log" -TotalCount 80
} else {
    Write-Host "logs\stata_env_test.log not found"
}
```

运行：

```powershell
powershell -ExecutionPolicy Bypass -File tools/check_local_env.ps1 *> logs/full_env_check.txt
```

## 9. 后续执行规则

后续所有 Python 命令请优先使用：

```powershell
conda run -n dml050 python ...
```

后续所有 Jupyter / nbstata 检查请优先使用：

```powershell
conda run -n dml050 jupyter ...
conda run -n dml050 python -m nbstata.install --sys-prefix
```

后续所有 Stata do 文件执行请优先使用：

```powershell
& "D:\stata19\StataMP-64.exe" /e do "path\to\file.do"
```

如果遇到 Stata 批处理参数问题，可以在不改变 Stata 路径的前提下，测试 `/e do` 和 `/b do` 两种方式。

请不要把 Stata 19 误认为没有安装。正确路径就是：

```powershell
D:\stata19\StataMP-64.exe
```

请不要把 `stata_dir` 写成：

```powershell
D:\stata19\StataMP-64.exe
```

`nbstata` 和 `pystata` 中的 Stata 目录应写成：

```powershell
D:\stata19
```

## 10. 成功标准

环境修复完成后，请在回复中报告下面几项：

* `conda run -n dml050 python --version` 的输出；
* `conda run -n dml050 python -c "import sys; print(sys.executable)"` 的输出；
* `conda run -n dml050 python -m pip show nbstata` 是否成功；
* `jupyter kernelspec list` 中是否出现 Stata / nbstata kernel；
* `tools/check_pystata.py` 是否能成功执行 `sysuse auto, clear` 和 `summarize price mpg`；
* `scripts/stata/00_env_test.do` 是否能通过 `D:\stata19\StataMP-64.exe` 执行；
* `logs/stata_env_test.log` 是否生成；
* 如果仍然失败，请给出精确报错，不要泛泛说找不到 Python 或找不到 Stata。

简言之，本机环境的核心信息是：Python 用 Anaconda 环境 `dml050`，Stata 用 `D:\stata19\StataMP-64.exe`，`nbstata` 的 `stata_dir` 应设为 `D:\stata19`，`edition` 应设为 `mp`。
