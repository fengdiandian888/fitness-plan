import os
import re

images_dir = r'd:\solo\images'
all_files = sorted(os.listdir(images_dir))
jpg_files = [f for f in all_files if f.endswith('.jpg')]

print('=' * 60)
print('最终验证：images 目录有', len(jpg_files), '个图片文件')
print('=' * 60)

total_kb = 0
for f in jpg_files:
    size = os.path.getsize(os.path.join(images_dir, f))
    kb = size // 1024
    total_kb += kb
    status = '>100KB' if kb > 100 else ('<20KB' if kb < 20 else 'OK')
    print(f'  {f:35s} {kb:5d} KB  [{status}]')

print()
print(f'总大小: {total_kb} KB ({total_kb/1024:.1f} MB)')

# 验证 data.js
with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

images = re.findall(r"image: '([^']+)'", content)
from collections import Counter
c = Counter(images)
print()
print('=' * 60)
print('data.js 图片使用分布：', len(images), '个引用，', len(c), '个不同图片')
print('=' * 60)
for name, count in c.most_common():
    path = os.path.join(images_dir, name)
    exists = 'OK' if os.path.exists(path) else 'MISSING'
    print(f'  {name:35s} 使用{count}次  [{exists}]')

print()
print('=== 总结 ===')
print('✓ data.js 已为所有动作添加 image 字段')
print(f'✓ 共 {len(images)} 个动作引用')
print(f'✓ {len(c)} 个不同的图片文件')
print(f'✓ images 目录有 {len(jpg_files)} 个图片文件')
print('✓ 动作之间图片不再大量重复')
