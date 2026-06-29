import re

with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r"image: '([^']+)'", content)
from collections import Counter
c = Counter(images)

print('=== 更新后 data.js 图片分析 ===')
print(f'总 image 字段: {len(images)}')
print(f'不同图片文件: {len(c)}')
print()
print('使用频率:')
for name, count in c.most_common():
    print(f'  {name}: {count}次')

# 检查哪些文件在 images 目录中存在
import os
existing = set(os.listdir(r'd:\solo\images'))
referenced = set(c.keys())
missing = []
for name in referenced:
    if name not in existing:
        missing.append(name)

if missing:
    print()
    print(f'!!! 有 {len(missing)} 个图片文件不在目录中:')
    for m in missing:
        print(f'  - {m}')
else:
    print()
    print('所有引用的图片都存在')
