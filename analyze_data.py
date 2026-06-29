import re

# 读取 data.js
with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 找出所有动作名及其当前 image 字段
pattern = r"name: '([^']+)',\s*sets: '([^']*)',\s*rest: '([^']*)'(?:,\s*image: '([^']*)')?"
matches = re.findall(pattern, content)

print("=== data.js 中所有动作 ===")
print(f'共找到 {len(matches)} 个动作对象')
print()

for i, (name, sets, rest, image) in enumerate(matches):
    img_str = image if image else '(无)'
    print(f'{i+1:2d}. {name:25s}  组数:{sets:8s}  休息:{rest:6s}  图片:{img_str}')

# 也找出早晨的字符串动作
morning_pattern = r"'([^']+分钟[^']+)'"  
morning_matches = re.findall(morning_pattern, content)
print()
print(f'字符串类型的动作: {len(morning_matches)} 个')
for m in morning_matches[:5]:
    print(f'  {m}')
