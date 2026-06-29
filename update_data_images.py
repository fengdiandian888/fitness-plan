import re

# 动作名 -> 图片文件名的映射（确保每个类别不同）
mapping = {
    # 拉日动作
    '哑铃俯身划船（主项）': 'bent-over-row.jpg',
    '弹力带高位下拉（固定门顶）': 'cable-pulldown.jpg',
    '弹力带面拉': 'band-external-rotation.jpg',
    '哑铃硬拉（轻重量）': 'deadlift.jpg',
    '哑铃弯举 + 锤式弯举（超级组）': 'bicep-curl.jpg',
    '弹力带肩外旋（肩袖保护）': 'band-external-rotation.jpg',
    
    # 推日动作
    '哑铃卧推（主项）': 'dumbbell-bench-press.jpg',
    '哑铃上斜推（枕头上垫高）': 'incline-dumbbell-press.jpg',
    '哑铃侧平举（轻量）': 'lateral-raise.jpg',
    '哑铃俯身臂屈伸（三头）': 'tricep-pushdown.jpg',
    '弹力带肩外旋 + 墙壁天使': 'rotator-cuff.jpg',
    
    # 腿日动作
    '哑铃酒杯深蹲（主项）': 'goblet-squat.jpg',
    '保加利亚分腿蹲': 'split-squat.jpg',
    '哑铃直腿硬拉（腘绳+臀）': 'single-leg-rdl.jpg',
    '单腿臀桥（瑜伽垫）': 'single-leg-glute-bridge.jpg',
    '提踵（小腿）': 'calf-raise.jpg',
    
    # 有氧
    '晨起低冲击有氧（跟练 25 分钟）': 'brisk-walk.jpg',
    '步行 / 通勤骑行': 'low-impact-cardio.jpg',
    '慢速散步': 'brisk-walk.jpg',
    
    # 全身/循环
    '哑铃全身循环（跟练 30 分钟）': 'fullbody-dumbbell.jpg',
    '靠墙静蹲（保护膝盖）': 'wall-sit.jpg',
    '单腿站立平衡': 'brisk-walk.jpg',
    
    # 核心
    '核心（15 分钟跟练）': 'core-workout.jpg',
    '核心（瑜伽垫）': 'core-workout.jpg',
    '平板支撑': 'plank.jpg',
    '死虫式': 'core-workout.jpg',
    '卷腹': 'crunch.jpg',
    '鸟狗式': 'plank.jpg',
    '超人式': 'core-workout.jpg',
    '侧平板': 'plank.jpg',
    
    # 恢复/热身
    '弹力带肩外旋（保护）': 'rotator-cuff.jpg',
    '全身动态拉伸（10 分钟）': 'stretch.jpg',
    '肩袖弹力带（倍他跟练）': 'band-external-rotation.jpg',
    '墙壁天使（胸椎活动）': 'rotator-cuff.jpg',
    '颈椎放松（自我按压）': 'stretch.jpg',
    '泡沫轴 · 腰背': 'foam-roller.jpg',
    
    # 其他常见弹力带肩外旋
    '弹力带肩外旋': 'band-external-rotation.jpg',
    '墙壁天使': 'rotator-cuff.jpg',
    
    # 热身
    '晨起低冲击热身（5 分钟）': 'warm-up.jpg',
}

# 读取 data.js
with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 为每个动作对象添加或更新 image 字段
# 模式：name: '...', sets: '...', rest: '...', 可能已有 image: '...'
pattern = r"(name: '([^']+)',\s*sets: '([^']*)',\s*rest: '([^']*)')(?:,\s*image: '[^']*')?"

def replacer(match):
    full = match.group(1)
    name = match.group(2)
    
    if name in mapping:
        img = mapping[name]
        return f"{full}, image: '{img}'"
    else:
        # 没在映射里，保持原样
        return match.group(0)

new_content = re.sub(pattern, replacer, content)

# 写回
with open(r'd:\solo\data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('=== data.js 更新完成 ===')
print(f'总共定义了 {len(mapping)} 个动作的图片映射')

# 验证：找出更新后仍没有 image 的动作
remaining = re.findall(r"name: '([^']+)',\s*sets: '[^']*',\s*rest: '[^']*'(?!,\s*image)", new_content)
if remaining:
    print(f'仍有 {len(remaining)} 个动作没有 image:')
    for name in remaining:
        print(f'  - {name}')
else:
    print('✓ 所有动作都有 image 字段')
