import re

with open(r'd:\solo\data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义每个动作名对应的图片文件
action_image_map = {
    # 拉日
    '哑铃俯身划船': 'bent-over-row.jpg',
    '弹力带面拉': 'band-external-rotation.jpg',
    '哑铃硬拉': 'deadlift.jpg',
    '哑铃弯举': 'bicep-curl.jpg',
    '哑铃弯举 + 锤式弯举': 'bicep-curl.jpg',
    
    # 推日
    '哑铃卧推': 'dumbbell-bench-press.jpg',
    '哑铃卧推（主项）': 'dumbbell-bench-press.jpg',
    '哑铃上斜推': 'incline-dumbbell-press.jpg',
    '哑铃上斜推（枕头上垫高）': 'incline-dumbbell-press.jpg',
    '哑铃侧平举': 'lateral-raise.jpg',
    '哑铃侧平举（轻量）': 'lateral-raise.jpg',
    '哑铃俯身臂屈伸': 'tricep-pushdown.jpg',
    '弹力带肩外旋 + 墙壁天使': 'shoulder-press.jpg',
    
    # 腿日
    '哑铃酒杯深蹲': 'goblet-squat.jpg',
    '哑铃酒杯深蹲（主项）': 'goblet-squat.jpg',
    '保加利亚分腿蹲': 'split-squat.jpg',
    '哑铃直腿硬拉': 'deadlift.jpg',
    '单腿臀桥': 'single-leg-glute-bridge.jpg',
    '单腿臀桥（瑜伽垫）': 'single-leg-glute-bridge.jpg',
    '提踵': 'split-squat.jpg',
    '提踵（小腿）': 'split-squat.jpg',
    
    # 有氧
    '晨起低冲击有氧': 'brisk-walk.jpg',
    '晨起低冲击有氧（跟练 25 分钟）': 'brisk-walk.jpg',
    '核心': 'core-workout.jpg',
    '核心（15 分钟跟练）': 'core-workout.jpg',
    '步行 / 通勤骑行': 'brisk-walk.jpg',
    
    # 恢复
    '全身动态拉伸': 'stretch.jpg',
    '全身动态拉伸（10 分钟）': 'stretch.jpg',
    '肩袖弹力带': 'band-external-rotation.jpg',
    '肩袖弹力带（倍他跟练）': 'band-external-rotation.jpg',
    '墙壁天使': 'band-external-rotation.jpg',
    '墙壁天使（胸椎活动）': 'band-external-rotation.jpg',
    '慢速散步': 'brisk-walk.jpg',
    
    # 全身
    '哑铃全身循环': 'fullbody-dumbbell.jpg',
    '哑铃全身循环（跟练 30 分钟）': 'fullbody-dumbbell.jpg',
    '靠墙静蹲': 'wall-sit.jpg',
    '靠墙静蹲（保护膝盖）': 'wall-sit.jpg',
    '核心（瑜伽垫）': 'core-workout.jpg',
    
    # 弹力带肩外旋出现多次
    '弹力带肩外旋': 'band-external-rotation.jpg',
    '弹力带肩外旋（肩袖保护）': 'band-external-rotation.jpg',
    '弹力带肩外旋（保护）': 'band-external-rotation.jpg',
    
    # 康复日
    '颈椎放松': 'stretch.jpg',
    '颈椎放松（自我按压）': 'stretch.jpg',
    '泡沫轴 · 腰背': 'foam-roller.jpg',
    '单腿站立平衡': 'brisk-walk.jpg',
}

# 为每个动作对象添加 image 字段
# 匹配模式：{ name: '动作名', ..., ...,
modified_content = content
count = 0

for action_name, image_file in action_image_map.items():
    # 找到包含这个动作名的对象，并添加 image 字段到 sets 字段后面
    # 模式： { name: '动作名', sets: 'x × y', rest: 'x',
    pattern = r"name: '" + re.escape(action_name) + r"',\s*sets: '([^']+)',\s*rest: '([^']+)'"
    replacement = f"name: '{action_name}', sets: '\\1', rest: '\\2', image: '{image_file}'"
    
    new_content, n = re.subn(pattern, replacement, modified_content)
    if n > 0:
        modified_content = new_content
        count += n
        print(f'已添加 image 字段: {action_name} ({n}处)')

with open(r'd:\solo\data.js', 'w', encoding='utf-8') as f:
    f.write(modified_content)

print(f'\n总计修改了 {count} 处动作对象')
