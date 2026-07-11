*======================================================================
* check_packages.do  —  T4 彩排前检查外部命令是否齐备
* 运行方式（工作目录 = demo/）：
*   "D:\stata19\StataMP-64.exe" /e do _dgp/check_packages.do
* 缺失的命令会打印对应的 ssc install 语句，照抄安装即可。
*======================================================================

clear all
set more off

di as text "==== 外部命令自检 ===="

foreach pkg in reghdfe ftools csdid drdid estout jwdid {
    capture which `pkg'
    if _rc {
        di as error  "缺失：`pkg'  ->  请运行:  ssc install `pkg', replace"
    }
    else {
        di as result "已安装：`pkg'"
    }
}

di as text "==== 自检完成 ===="
di as text "注：estout 包内含 esttab；jwdid 为可选（缺失时分析可跳过）。"
