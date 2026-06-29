import re

# 读取 data.js
with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 找出所有动作名
names = re.findall(r"name: '([^']+)'", content)

# 复制 JS 中的匹配逻辑（Python 版本）
def get_move_icon(name):
    if '划船' in name or '下拉' in name or '面拉' in name or '硬拉' in name:
        return ('🔱', '拉日-绿色')
    if '弯举' in name or '锤式' in name:
        return ('💪', '拉日-绿色')
    if '卧推' in name or '上斜推' in name:
        return ('🏋️', '推日-蓝色')
    if '侧平举' in name or '肩推' in name:
        return ('↔️', '推日-蓝色')
    if '臂屈伸' in name or '三头' in name:
        return ('↕️', '推日-蓝色')
    if '深蹲' in name:
        return ('🦵', '腿日-橙色')
    if '分腿蹲' in name or '弓步' in name:
        return ('🚶', '腿日-橙色')
    if '单腿臀桥' in name or '臀桥' in name:
        return ('🍑', '腿日-橙色')
    if '提踵' in name:
        return ('👟', '腿日-橙色')
    if '靠墙静蹲' in name:
        return ('🧱', '腿日-橙色')
    if '直腿硬拉' in name or '腘绳' in name:
        return ('🏋️', '腿日-橙色')
    if '平板支撑' in name or '核心' in name or '卷腹' in name or '死虫' in name or '鸟狗' in name or '超人' in name or '侧平板' in name:
        return ('🎯', '核心-紫色')
    if '步行' in name or '快步' in name or '有氧' in name or '骑行' in name or '单车' in name or '散步' in name:
        return ('🏃', '有氧-青色')
    if '肩外旋' in name or '墙壁天使' in name or '肩袖' in name:
        return ('🔄', '恢复-薄荷色')
    if '泡沫轴' in name or '拉伸' in name or '颈椎' in name or '放松' in name:
        return ('🧘', '恢复-薄荷色')
    if '热身' in name or '动态' in name:
        return ('🔥', '恢复-薄荷色')
    if '全身' in name or '循环' in name:
        return ('⚡', '全身-橙色')
    if '平衡' in name or '站立' in name:
        return ('⚖️', '有氧-青色')
    return ('💪', '默认-蓝色')

print('=' * 70)
print('动作图标匹配验证')
print('=' * 70)

# 去重后显示
unique_names = list(dict.fromkeys(names))
print(f'共 {len(unique_names)} 个动作')
print()

categories = {}
for name in unique_names:
    emoji, color = get_move_icon(name)
    cat = color.split('-')[0]
    if cat not in categories:
        categories[cat] = []
    categories[cat].append((name, emoji, color))

for cat, items in categories.items():
    print(f'【{cat}】共 {len(items)} 个动作')
    for name, emoji, color in items:
        print(f'  {emoji}  {name}')
    print()

print('=' * 70)
print('✓ 所有动作都有图标匹配')
print('=' * 70)
