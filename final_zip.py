import zipfile
import os
import sys

base_dir = r'd:\solo'
zip_name = os.path.join(base_dir, '减脂App_完整项目_v10.zip')

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

output = []

if os.path.exists(zip_name):
    os.remove(zip_name)
    output.append('Removed existing zip')

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
    for f in files:
        fp = os.path.join(base_dir, f)
        if os.path.exists(fp):
            zf.write(fp, arcname=f)
            output.append(f'Added: {f}')
        else:
            output.append(f'MISSING: {f}')

if os.path.exists(zip_name):
    size = os.path.getsize(zip_name)
    output.append(f'SUCCESS! Created: {zip_name}')
    output.append(f'Size: {size} bytes')
else:
    output.append('FAILED! Zip not created')

# Write to log file
log_path = os.path.join(base_dir, 'zip_result.txt')
with open(log_path, 'w') as f:
    f.write('\n'.join(output))

# Also print to stdout
print('\n'.join(output))
