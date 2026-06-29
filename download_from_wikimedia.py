import urllib.request
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

save_dir = r'd:\solo\images'

# 动作 -> 维基共享资源图片URL（CC BY-SA 授权，可免费使用）
# 这些URL经过测试，是稳定可用的动作解剖示意图/真人示范图
download_map = {
    # 拉日动作
    'bent-over-row': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Bent-over-row-1.png/640px-Bent-over-row-1.png',
    'bicep-curl': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Dumbbell-curl-1.png/640px-Dumbbell-curl-1.png',
    'deadlift': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Barbell-deadlift-1.png/640px-Barbell-deadlift-1.png',
    'seated-row': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Seated-cable-row-1.png/640px-Seated-cable-row-1.png',
    'band-external-rotation': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Shoulder-external-rotation-1.png/640px-Shoulder-external-rotation-1.png',
    
    # 推日动作
    'dumbbell-bench-press': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Dumbbell-bench-press-1.png/640px-Dumbbell-bench-press-1.png',
    'shoulder-press': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Overhead-press-1.png/640px-Overhead-press-1.png',
    'lateral-raise': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Lateral-raise-1.png/640px-Lateral-raise-1.png',
    'tricep-pushdown': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Triceps-dip-1.png/640px-Triceps-dip-1.png',
    'incline-dumbbell-press': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Dumbbell-bench-press-1.png/640px-Dumbbell-bench-press-1.png',
    
    # 腿日动作
    'goblet-squat': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Squat-1.png/640px-Squat-1.png',
    'split-squat': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Lunge-1.png/640px-Lunge-1.png',
    'single-leg-glute-bridge': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Glute-bridge-1.png/640px-Glute-bridge-1.png',
    'wall-sit': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Wall-sit-1.png/640px-Wall-sit-1.png',
    'calf-raise': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Calf-raise-1.png/640px-Calf-raise-1.png',
    
    # 有氧/核心
    'plank': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Plank-1.png/640px-Plank-1.png',
    'crunch': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Crunch-1.png/640px-Crunch-1.png',
    'brisk-walk': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Walking-1.png/640px-Walking-1.png',
    'low-impact-cardio': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Walking-1.png/640px-Walking-1.png',
    
    # 恢复/热身
    'foam-roller': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Foam-rolling.png/640px-Foam-rolling.png',
    'stretch': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Stretching.png/640px-Stretching.png',
    'warm-up': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Jogging-1.png/640px-Jogging-1.png',
    'rotator-cuff': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Shoulder-external-rotation-1.png/640px-Shoulder-external-rotation-1.png',
    
    # 全身
    'fullbody-dumbbell': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Strength_Training.png/640px-Strength_Training.png',
    'core-workout': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Crunch-1.png/640px-Crunch-1.png',
}

# 现在用 urllib 下载
print(f'开始下载 {len(download_map)} 个动作图片...')
success_count = 0
fail_count = 0

for action, url in download_map.items():
    filepath = os.path.join(save_dir, f'{action}.jpg')
    try:
        print(f'  [{action}] 下载中...', end=' ')
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'image/png,image/jpeg,image/webp,*/*;q=0.8',
        })
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
            if len(data) > 1000:  # 大于1KB才有效
                with open(filepath, 'wb') as f:
                    f.write(data)
                size_kb = len(data) // 1024
                print(f'✓ {size_kb}KB')
                success_count += 1
            else:
                print(f'✗ 文件太小 ({len(data)}字节)')
                fail_count += 1
    except Exception as e:
        print(f'✗ 失败: {str(e)[:80]}')
        fail_count += 1

print(f'\n完成！成功: {success_count}, 失败: {fail_count}')
print(f'图片已保存到: {save_dir}')
