# -*- coding: utf-8 -*-
# 提取所有需要配图的动作清单，去重
import re

data_js = open(r'd:\solo\data.js', 'r', encoding='utf-8').read()

# 提取 name: 后面的中文动作名和对应的 image: 文件名
pattern = r"name:\s*'([^']+)'.*?image:\s*'([^']+)'"
matches = re.findall(pattern, data_js, re.DOTALL)

# 去重（按 image 文件名去重，保留第一个）
seen_images = set()
unique_actions = []
for name, image in matches:
    if image not in seen_images:
        seen_images.add(image)
        unique_actions.append((name, image))

print(f"找到 {len(matches)} 个动作条目，去重后 {len(unique_actions)} 个独特动作：")
print()
for i, (name, image) in enumerate(unique_actions, 1):
    print(f"{i}. {name:30s} -> images/{image}")
