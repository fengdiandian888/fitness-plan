import zipfile
import os

# 设置路径
base_dir = r'd:\solo'
os.chdir(base_dir)

# 文件列表
files_to_pack = [
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
zip_filename = os.path.join(base_dir, '减脂App_完整项目_v10.zip')

# 删除旧文件
if os.path.exists(zip_filename):
    os.remove(zip_filename)
    print(f'Removed old zip: {zip_filename}')

# 创建新压缩包
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
    for filename in files_to_pack:
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            zf.write(filename)
            print(f'Added: {filename}')
        else:
            print(f'SKIPPED (missing): {filename}')

# 验证
if os.path.exists(zip_filename):
    size = os.path.getsize(zip_filename)
    print(f'\nSUCCESS! Created: {zip_filename}')
    print(f'Size: {size / 1024:.2f} KB')
    
    # 列出内容
    with zipfile.ZipFile(zip_filename, 'r') as zf:
        print(f'Files in zip: {len(zf.namelist())}')
        for name in zf.namelist():
            info = zf.getinfo(name)
            print(f'  - {name} ({info.file_size} bytes)')
else:
    print(f'\nFAILED! Zip file not created')
