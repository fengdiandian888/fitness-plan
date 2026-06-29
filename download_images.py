import urllib.request
import os
import ssl

# 忽略SSL证书验证问题
ssl._create_default_https_context = ssl._create_unverified_context

save_dir = r'd:\solo\images'
os.makedirs(save_dir, exist_ok=True)

# 动作图片列表：(文件名, 图片URL)
images = [
    # 拉日动作
    ('01-dumbbell-row.jpg', 'https://aka.doubaocdn.com/s/5vmW1wfTUt'),
    ('02-bicep-curl.jpg', 'https://aka.doubaocdn.com/s/ZgOY1wfTUt'),
    ('03-band-external-rotation.jpg', 'https://aka.doubaocdn.com/s/yYVY1wfTUF'),
    ('04-deadlift.jpg', 'https://aka.doubaocdn.com/s/ppvR1wfTUF'),
    
    # 推日动作
    ('05-dumbbell-bench-press.jpg', 'https://aka.doubaocdn.com/s/yBkY1wfTUF'),
    ('06-dumbbell-shoulder-press.jpg', 'https://aka.doubaocdn.com/s/06vR1wfTUF'),
    ('07-lateral-raise.jpg', 'https://aka.doubaocdn.com/s/hZ3Y1wfTUF'),
    ('08-tricep-pushdown.jpg', 'https://aka.doubaocdn.com/s/49mY1wfTUF'),
    
    # 腿日动作
    ('09-goblet-squat.jpg', 'https://aka.doubaocdn.com/s/Gf5w1wfTOF'),
    ('10-dumbbell-lunge.jpg', 'https://aka.doubaocdn.com/s/VHMV1wfTOF'),
    ('11-glute-bridge.jpg', 'https://aka.doubaocdn.com/s/DJSl1wfTOF'),
    ('12-wall-sit.jpg', 'https://aka.doubaocdn.com/s/H0V91wfTOF'),
    
    # 核心/有氧
    ('13-plank.jpg', 'https://aka.doubaocdn.com/s/3V2Y1wfTUF'),
    ('14-resistance-band.jpg', 'https://aka.doubaocdn.com/s/kwvY1wfTUF'),
    ('15-brisk-walking.jpg', 'https://aka.doubaocdn.com/s/Donv1wfTOF'),
    ('16-foam-roller.jpg', 'https://aka.doubaocdn.com/s/erCd1wfTOF'),
]

for filename, url in images:
    filepath = os.path.join(save_dir, filename)
    try:
        urllib.request.urlretrieve(url, filepath)
        size = os.path.getsize(filepath)
        print(f'OK  {filename}  ({size} bytes)')
    except Exception as e:
        print(f'FAIL {filename}: {e}')

print('\n下载完成！')
