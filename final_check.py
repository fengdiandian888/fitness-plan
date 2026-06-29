import os

images_dir = r'd:\solo\images'
required_images = [
    'bent-over-row.jpg', 'bicep-curl.jpg', 'deadlift.jpg', 
    'seated-row.jpg', 'band-external-rotation.jpg',
    'dumbbell-bench-press.jpg', 'shoulder-press.jpg', 'lateral-raise.jpg', 
    'tricep-pushdown.jpg', 'incline-dumbbell-press.jpg',
    'goblet-squat.jpg', 'split-squat.jpg', 'single-leg-rdl.jpg', 
    'single-leg-glute-bridge.jpg', 'wall-sit.jpg', 'calf-raise.jpg',
    'plank.jpg', 'crunch.jpg', 'brisk-walk.jpg',
    'core-workout.jpg', 'low-impact-cardio.jpg',
    'foam-roller.jpg', 'stretch.jpg', 'rotator-cuff.jpg',
    'warm-up.jpg', 'cable-pulldown.jpg',
    'fullbody-dumbbell.jpg',
]

print('检查 data.js 引用的图片文件：')
print('-' * 60)
missing = []
for img in required_images:
    path = os.path.join(images_dir, img)
    if os.path.exists(path):
        size = os.path.getsize(path) // 1024
        print(f'OK  {img:35s} {size:5d} KB')
    else:
        print(f'MISSING {img}')
        missing.append(img)

if missing:
    print()
    print(f'!!! 缺少 {len(missing)} 个图片文件')
    for m in missing:
        print(f'  - {m}')
else:
    print()
    print('所有图片都已就位！')

# 现在检查 data.js 的实际引用
import re
with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

images_in_data = set(re.findall(r"image: '([^']+)'", content))
print()
print(f'data.js 中引用了 {len(images_in_data)} 个不同的图片')
for img in sorted(images_in_data):
    path = os.path.join(images_dir, img)
    if os.path.exists(path):
        size = os.path.getsize(path) // 1024
        print(f'  {img:35s} {size:5d} KB')
    else:
        print(f'  {img} - 不存在')
