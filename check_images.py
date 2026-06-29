import re
from collections import Counter

content = open(r'd:\solo\data.js', encoding='utf-8').read()
images = re.findall(r"image: '([^']+)'", content)
c = Counter(images)

print('=== data.js 中 image 字段分析 ===')
print(f'总 image 字段数: {len(images)}')
print(f'不同的图片文件: {len(c)}')
print()
print('图片使用频率:')
for name, count in c.most_common(40):
    print(f'  {name}: {count}次')

print()
print('=== images 目录中的实际文件 ===')
import os
files = os.listdir(r'd:\solo\images')
jpg_files = [f for f in files if f.endswith('.jpg')]
print(f'目录中有 {len(jpg_files)} 个 JPG 文件')

# 检查哪些图片文件在 data.js 中被引用
referenced = set(c.keys())
existing = set(jpg_files)
print(f'data.js 引用的: {len(referenced)}')
print(f'实际存在的: {len(existing)}')
print(f'引用但不存在: {referenced - existing}')
