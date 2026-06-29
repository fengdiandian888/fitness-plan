@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ========================================
echo     减脂App - 项目打包工具
echo ========================================
echo.

if exist "减脂App_完整项目_v10.zip" (
    echo 删除旧压缩包...
    del "减脂App_完整项目_v10.zip"
)

echo 创建压缩包...
powershell -Command "Compress-Archive -Path 'index.html','今日计划.html','减脂训练日跟练_三分化.html','减脂完整教程_饮食运动作息动作库.html','减脂全面计划.html','每周小结.html','视频管理后台.html','data.js','shared.js','gist-storage.js','serviceWorker.js','shared.css','manifest.json','icon-192.png','icon-512.png','减脂App软件说明书.md','项目完整文档.md' -DestinationPath '减脂App_完整项目_v10.zip' -Force"

if exist "减脂App_完整项目_v10.zip" (
    echo.
    echo ✅ 打包成功！
    echo.
    echo 压缩包位置: %~dp0减脂App_完整项目_v10.zip
    
    for %%f in ("减脂App_完整项目_v10.zip") do (
        echo 文件大小: %%~zf 字节
    )
    
    echo.
    echo 按任意键退出...
    pause >nul
) else (
    echo.
    echo ❌ 打包失败！
    echo 请检查文件是否存在。
    echo.
    echo 按任意键退出...
    pause >nul
)