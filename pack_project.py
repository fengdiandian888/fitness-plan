import zipfile
import os

# 设置工作目录
os.chdir(r'd:\solo')

# 要打包的文件列表
files = [
    'index.html',
    '今日计划.html',
    '减脂训练日跟练_三分化.html',
    '减脂完整教程_饮食运动作息动作库.html',
    '减脂全面计划.html',
    '每周小结.html',
    '视频管理后台.html',
    'data.js',
    'shared.js',
    'gist-storage.js',
    'serviceWorker.js',
    'shared.css',
    'manifest.json',
    'icon-192.png',
    'icon-512.png',
    '减脂App软件说明书.md',
    '项目完整文档.md'
]

# 创建压缩包
zip_filename = '减脂App_完整项目_v10.zip'
z = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

for f in files:
    if os.path.exists(f):
        z.write(f)
        print(f'Added: {f}')
    else:
        print(f'Missing: {f}')

z.close()
print(f'\nCreated: {zip_filename}')
print(f'Total files: {len(files)}')
