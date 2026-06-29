import urllib.request
import os
import ssl
import hashlib

ssl._create_default_https_context = ssl._create_unverified_context

save_dir = r'd:\solo\images'
os.makedirs(save_dir, exist_ok=True)

# 从 Wikimedia Commons 和其他可靠源下载真正的健身动作图片
# 注意：这些是免费授权的图片（CC BY-SA 或公共领域）

download_list = [
    # 1. 哑铃俯身划船 / 背训
    ('bent-over-row.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Bent-over-row-1.png/640px-Bent-over-row-1.png'),
    
    # 2. 哑铃二头弯举
    ('bicep-curl.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Dumbbell-curl-1.png/640px-Dumbbell-curl-1.png'),
    
    # 3. 哑铃卧推
    ('dumbbell-bench-press.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Dumbbell-bench-press-1.png/640px-Dumbbell-bench-press-1.png'),
    
    # 4. 深蹲
    ('goblet-squat.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Squat-1.png/640px-Squat-1.png'),
    
    # 5. 分腿蹲/弓步
    ('split-squat.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Lunge-1.png/640px-Lunge-1.png'),
    
    # 6. 硬拉
    ('deadlift.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Barbell-deadlift-1.png/640px-Barbell-deadlift-1.png'),
    
    # 7. 单腿臀桥
    ('single-leg-glute-bridge.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Glute-bridge-1.png/640px-Glute-bridge-1.png'),
    
    # 8. 肩外旋/弹力带
    ('band-external-rotation.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Shoulder-external-rotation-1.png/640px-Shoulder-external-rotation-1.png'),
    
    # 9. 平板支撑
    ('plank.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Plank-1.png/640px-Plank-1.png'),
    
    # 10. 侧平举
    ('lateral-raise.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Lateral-raise-1.png/640px-Lateral-raise-1.png'),
    
    # 11. 肩推
    ('shoulder-press.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Overhead-press-1.png/640px-Overhead-press-1.png'),
    
    # 12. 泡沫轴
    ('foam-roller.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Foam-rolling.png/640px-Foam-rolling.png'),
    
    # 13. 靠墙静蹲
    ('wall-sit.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Wall-sit-1.png/640px-Wall-sit-1.png'),
    
    # 14. 快步走
    ('brisk-walk.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Walking-1.png/640px-Walking-1.png'),
    
    # 15. 俯身臂屈伸（三头）
    ('tricep-pushdown.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Triceps-dip-1.png/640px-Triceps-dip-1.png'),
    
    # 16. 坐姿划船
    ('seated-row.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Seated-cable-row-1.png/640px-Seated-cable-row-1.png'),
    
    # 17. 卷腹
    ('crunch.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Crunch-1.png/640px-Crunch-1.png'),
    
    # 18. 提踵
    ('calf-raise.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Calf-raise-1.png/640px-Calf-raise-1.png'),
    
    # 19. 全身哑铃循环
    ('fullbody-dumbbell.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Strength_Training.png/640px-Strength_Training.png'),
    
    # 20. 上斜哑铃卧推
    ('incline-dumbbell-press.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Dumbbell-bench-press-1.png/640px-Dumbbell-bench-press-1.png'),
]

success = 0
failed = 0

for filename, url in download_list:
    filepath = os.path.join(save_dir, filename)
    try:
        print(f'下载中: {filename} ...')
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            with open(filepath, 'wb') as f:
                f.write(data)
        size = os.path.getsize(filepath)
        if size > 2000:  # 大于2KB才有效
            print(f'  ✓ OK ({size} bytes)')
            success += 1
        else:
            print(f'  ✗ 文件太小，可能下载失败 ({size} bytes)')
            failed += 1
    except Exception as e:
        print(f'  ✗ 失败: {e}')
        failed += 1

print(f'\n完成！成功: {success}, 失败: {failed}')

# 为没有特定图片的动作提供合理的替换
print('\n现在为剩余动作分配图片...')
