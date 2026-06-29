import subprocess
import os

os.chdir(r'd:\solo')

cmd = [
    'powershell',
    '-Command',
    'Compress-Archive -Path "index.html","今日计划.html","减脂训练日跟练_三分化.html","减脂完整教程_饮食运动作息动作库.html","减脂全面计划.html","每周小结.html","视频管理后台.html","data.js","shared.js","gist-storage.js","serviceWorker.js","shared.css","manifest.json","icon-192.png","icon-512.png","减脂App软件说明书.md","项目完整文档.md" -DestinationPath "减脂App_完整项目_v10.zip" -Force'
]

result = subprocess.run(cmd, capture_output=True, text=True)
print(f'Exit code: {result.returncode}')
print(f'Stdout: {result.stdout}')
print(f'Stderr: {result.stderr}')

if os.path.exists('减脂App_完整项目_v10.zip'):
    print(f'\nSUCCESS! Zip file created')
    print(f'Size: {os.path.getsize("减脂App_完整项目_v10.zip")} bytes')
else:
    print('\nFAILED! Zip file not created')
