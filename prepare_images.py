import os
import shutil

save_dir = r'd:\solo\images'

# 清理测试文件
for f in ['test1.png', '01-bent-over-row.jpg']:
    p = os.path.join(save_dir, f)
    if os.path.exists(p):
        os.remove(p)
        print(f'删除 {f}')

# 现有图片
print('\n现有图片：')
for f in sorted(os.listdir(save_dir)):
    size = os.path.getsize(os.path.join(save_dir, f))
    print(f'  {f} ({size} bytes)')

# 为所有需要的动作创建图片文件（复用现有图片）
print('\n创建动作图片...')

# 映射：动作名 -> 源图片
mappings = {
    # 拉日
    'bent-over-row': '01-dumbbell-row.jpg',      # 俯身划船
    'bicep-curl': '02-bicep-curl.jpg',          # 二头弯举
    'pull-up': '01-dumbbell-row.jpg',           # 下拉/背
    'deadlift': '09-goblet-squat.jpg',          # 硬拉（用深蹲图片代替）
    'seated-row': '01-dumbbell-row.jpg',        # 坐姿划船
    'cable-pulldown': '01-dumbbell-row.jpg',    # 高位下拉
    
    # 推日
    'dumbbell-bench-press': '02-bicep-curl.jpg',  # 哑铃卧推
    'shoulder-press': '02-bicep-curl.jpg',      # 哑铃肩推
    'lateral-raise': '02-bicep-curl.jpg',       # 侧平举
    'tricep-pushdown': '02-bicep-curl.jpg',     # 俯身臂屈伸
    'incline-dumbbell-press': '02-bicep-curl.jpg',  # 上斜推
    
    # 腿日
    'goblet-squat': '09-goblet-squat.jpg',      # 高脚杯深蹲
    'split-squat': '10-dumbbell-lunge.jpg',     # 分腿蹲
    'single-leg-rdl': '10-dumbbell-lunge.jpg',  # 单腿硬拉
    'single-leg-glute-bridge': '11-glute-bridge.jpg', # 单腿臀桥
    
    # 全身/核心
    'fullbody-dumbbell': '01-dumbbell-row.jpg', # 全身哑铃循环
    'wall-sit': '12-wall-sit.jpg',              # 靠墙静蹲
    'plank': '11-glute-bridge.jpg',             # 平板支撑
    'core-workout': '11-glute-bridge.jpg',      # 核心训练
    'crunch': '11-glute-bridge.jpg',            # 卷腹
    
    # 有氧
    'brisk-walk': '15-brisk-walking.jpg',       # 快步走
    'low-impact-cardio': '15-brisk-walking.jpg', # 低冲击有氧
    
    # 恢复/热身
    'foam-roller': '16-foam-roller.jpg',        # 泡沫轴
    'band-external-rotation': '02-bicep-curl.jpg', # 弹力带肩外旋
    'warm-up': '15-brisk-walking.jpg',          # 热身
    'stretch': '16-foam-roller.jpg',            # 拉伸
    'rotator-cuff': '02-bicep-curl.jpg',        # 肩袖
}

for action_name, source_file in mappings.items():
    src = os.path.join(save_dir, source_file)
    dst = os.path.join(save_dir, f'{action_name}.jpg')
    
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'OK  {action_name}.jpg <- {source_file}')
    else:
        print(f'WARN 源文件不存在: {source_file}')

print(f'\n完成！images目录共有 {len(os.listdir(save_dir))} 个文件')
