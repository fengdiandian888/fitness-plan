import zipfile
import os

log_path = r'd:\solo\zip_log.txt'
zip_path = r'd:\solo\减脂App_完整项目_v10.zip'

with open(log_path, 'w') as log:
    log.write(f'Starting zip creation at {zip_path}\n')
    
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
    
    log.write(f'Files to pack: {len(files)}\n')
    
    if os.path.exists(zip_path):
        os.remove(zip_path)
        log.write('Removed existing zip\n')
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                full_path = os.path.join(r'd:\solo', f)
                if os.path.exists(full_path):
                    zf.write(full_path, arcname=f)
                    log.write(f'Added: {f}\n')
                else:
                    log.write(f'Missing: {f}\n')
        
        if os.path.exists(zip_path):
            size = os.path.getsize(zip_path)
            log.write(f'SUCCESS! Zip created at {zip_path}\n')
            log.write(f'Size: {size} bytes\n')
        else:
            log.write('FAILED! Zip file not found after creation\n')
            
    except Exception as e:
        log.write(f'ERROR: {str(e)}\n')
