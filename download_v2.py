import urllib.request
import os
import ssl
import shutil

ssl._create_default_https_context = ssl._create_unverified_context

save_dir = r'd:\solo\images'

# 用多种可靠的图片源（多个备用方案，失败时自动尝试下一个
image_sources = {
    # 拉日
    'bent-over-row': [
        'https://aka.doubaocdn.com/s/me7K1wfTOD',
        'https://aka.doubaocdn.com/s/blX61wfTOD',
    ],
    'bicep-curl': [
        'https://aka.doubaocdn.com/s/Mr531wfTOE',
        'https://aka.doubaocdn.com/s/SUT91wfTOE',
    ],
    'deadlift': [
        'https://aka.doubaocdn.com/s/ppvR1wfTUF',
    ],
    'seated-row': [
        'https://aka.doubaocdn.com/s/me7K1wfTOD',
    ],
    'band-external-rotation': [
        'https://aka.doubaocdn.com/s/sjRu1wfTOE',
        'https://aka.doubaocdn.com/s/0UY41wfTOE',
    ],
    
    # 推日
    'dumbbell-bench-press': [
        'https://aka.doubaocdn.com/s/yBkY1wfTUF',
    ],
    'shoulder-press': [
        'https://aka.doubaocdn.com/s/06vR1wfTUF',
    ],
    'lateral-raise': [
        'https://aka.doubaocdn.com/s/hZ3Y1wfTUF',
    ],
    'tricep-pushdown': [
        'https://aka.doubaocdn.com/s/49mY1wfTUF',
    ],
    'incline-dumbbell-press': [
        'https://aka.doubaocdn.com/s/yBkY1wfTUF',
    ],
    
    # 腿日
    'goblet-squat': [
        'https://aka.doubaocdn.com/s/Gf5w1wfTOF',
        'https://aka.doubaocdn.com/s/PONb1wfTOF',
    ],
    'split-squat': [
        'https://aka.doubaocdn.com/s/VHMV1wfTOF',
        'https://aka.doubaocdn.com/s/jD2o1wfTOF',
    ],
    'single-leg-glute-bridge': [
        'https://aka.doubaocdn.com/s/DJSl1wfTOF',
    ],
    'wall-sit': [
        'https://aka.doubaocdn.com/s/H0V91wfTOF',
    ],
    'calf-raise': [
        'https://aka.doubaocdn.com/s/erCd1wfTOF',
    ],
    
    # 有氧/核心
    'plank': [
        'https://aka.doubaocdn.com/s/PONb1wfTOF',
        'https://aka.doubaocdn.com/s/ffEk1wfTOF',
    ],
    'core-workout': [
        'https://aka.doubaocdn.com/s/3V2Y1wfTUF',
    ],
    'crunch': [
        'https://aka.doubaocdn.com/s/3V2w1wfTUF',
    ],
    'brisk-walk': [
        'https://aka.doubaocdn.com/s/Donv1wfTOF',
    ],
    
    # 恢复
    'foam-roller': [
        'https://aka.doubaocdn.com/s/KqVO1wfTOE',
        'https://aka.doubaocdn.com/s/Wh4s1wfTOE',
    ],
    'stretch': [
        'https://aka.doubaocdn.com/s/AB6R1wfTOE',
    ],
    'warm-up': [
        'https://aka.doubaocdn.com/s/Donv1wfTOF',
    ],
    'rotator-cuff': [
        'https://aka.doubaocdn.com/s/AB6R1wfTOE',
    ],
    
    # 全身
    'fullbody-dumbbell': [
        'https://aka.doubaocdn.com/s/Gf5w1wfTOF',
    ],
    'low-impact-cardio': [
        'https://aka.doubaocdn.com/s/Donv1wfTOF',
    ],
}

# 清理旧文件（保留原始下载的大文件）
# 现在下载并验证每个动作的图片
success = 0
failed = 0

for action_name, urls in image_sources.items():
    filepath = os.path.join(save_dir, f'{action_name}.jpg')
    downloaded = False
    
    for url in urls:
        try:
            print(f'下载 {action_name}: 尝试: {url.split("/")[-1][:20]}...')
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'image/png,image/jpeg,image/webp,*/*',
            })
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                if len(data) > 3000:  # 大于3KB
                    with open(filepath, 'wb') as f:
                        f.write(data)
                    size_kb = len(data) // 1024
                    print(f'  ✓ {size_kb}KB')
                    success += 1
                    downloaded = True
                    break
                else:
                    print(f'  × 文件太小 ({len(data)}字节)')
        except Exception as e:
            print(f'  × 失败: {str(e)[:50]}')
            continue
    
    if not downloaded:
        print(f'  ! {action_name} 所有源都失败')
        failed += 1

print(f'\n========== 完成 ==========')
print(f'成功: {success} / {len(image_sources)}')
print(f'失败: {failed}')
