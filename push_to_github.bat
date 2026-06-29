@echo off
echo 请输入你的 GitHub Personal Access Token：
set /p token=
echo.
d:\solo\git\bin\git.exe push https://fengdiandian888:%token%@github.com/fengdiandian888/fitness-plan.git main
pause
