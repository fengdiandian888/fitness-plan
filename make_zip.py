import zipfile
import os

os.chdir(r'd:\solo')

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

zip_name = '减脂App_完整项目_v10.zip'

if os.path.exists(zip_name):
    os.remove(zip_name)
    print('Removed existing zip')

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for f in files:
        if os.path.exists(f):
            zf.write(f)
            print(f'Added: {f}')
        else:
            print(f'MISSING: {f}')

print(f'\n=== Created: {zip_name} ===')
print(f'Size: {os.path.getsize(zip_name) / 1024:.1f} KB')
