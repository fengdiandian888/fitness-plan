# -*- coding: utf-8 -*-
"""
为所有健身动作生成高质量 AI 图片
风格：真实人体示范 + 简洁清晰的动作姿态 + 专业健身教练风格
"""
import requests
import os
import time

# Trae 内置图片生成 API
API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

# 统一风格前缀 - 真实健身教练示范
STYLE_PREFIX = "Professional fitness instructor demonstrating exercise, photorealistic, clean white studio background, perfect form demonstration, side view showing full body, wearing athletic wear, professional lighting, high resolution, fitness photos, 4k, sharp focus, no watermark, professional photography, commercial fitness photography"
STYLE_SUFFIX = ", professional fitness photography, side view full body demonstration, clean white background, perfect exercise form, professional lighting, photorealistic, sharp focus, no watermark"

# 动作清单：(中文名称, 图片文件名, 英文 prompt 描述
ACTIONS = [
    # 拉日
    ("哑铃俯身划船", "bent-over-row.jpg",
     "professional fitness coach doing dumbbell bent-over row exercise, man holding dumbbells in both hands, torso bent forward 45 degrees, back straight pulling dumbbells to hips, demonstrating proper rowing motion, side view"),
    ("弹力带高位下拉", "cable-pulldown.jpg",
     "fitness person doing resistance band lat pulldown exercise, pulling band overhead pulling down to chest, back straight, demonstrating proper form side view"),
    ("弹力带面拉", "facepull.jpg",
     "fitness coach doing resistance band face pull exercise, pulling band to forehead, elbows up, rear deltoid activation, side view demonstrating"),
    ("哑铃硬拉", "deadlift.jpg",
     "professional fitness instructor demonstrating dumbbell deadlift, standing position holding dumbbells, back straight, hips back, showing proper deadlift form, side view"),
    ("哑铃弯举", "bicep-curl.jpg",
     "fitness coach doing alternating dumbbell bicep curl exercise, arms curling dumbbells up, showing proper bicep curl form, front view"),
    # 推日
    ("哑铃卧推", "dumbbell-bench-press.jpg",
     "professional fitness coach doing dumbbell bench press exercise, lying on bench, pressing dumbbells up from chest, demonstrating proper bench press form"),
    ("哑铃上斜推", "incline-dumbbell-press.jpg",
     "fitness person doing incline dumbbell press on incline bench, upper chest exercise, pressing dumbbells upward, demonstrating proper form side view"),
    ("哑铃侧平举", "lateral-raise.jpg",
     "fitness coach doing dumbbell lateral raise, arms raising dumbbells out to sides like wings, shoulder exercise, demonstrating proper lateral raise form front view"),
    ("哑铃俯身臂屈伸", "tricep-pushdown.jpg",
     "fitness person doing triceps dumbbell kickback exercise, bent over position, extending arm back showing tricep extension, demonstrating proper triceps form side view"),
    ("肩外旋", "rotator-cuff.jpg",
     "professional fitness coach doing shoulder external rotation with resistance band, arm at side elbow 90 degrees rotating externally, demonstrating proper shoulder rehab exercise front view"),
    # 腿日
    ("哑铃酒杯深蹲", "goblet-squat.jpg",
     "fitness coach doing goblet squat exercise, holding one dumbbell at chest, squatting down, showing proper squat form, side view"),
    ("保加利亚分腿蹲", "split-squat.jpg",
     "fitness person doing bulgarian split squat exercise, back foot elevated on bench, front leg lunging, demonstrating proper single leg squat form side view"),
    ("哑铃直腿硬拉", "single-leg-rdl.jpg",
     "professional fitness coach doing romanian deadlift exercise with dumbbells, keeping legs straight or slightly bent, hinging at hips lowering dumbbells to shins, showing hamstring and glute activation side view"),
    ("单腿臀桥", "single-leg-glute-bridge.jpg",
     "fitness person doing single leg glute bridge exercise on floor, one leg extended, hips lifting up, demonstrating proper glute bridge form side view"),
    ("提踵", "calf-raise.jpg",
     "fitness coach doing calf raise exercise, standing on toes elevating heels, showing proper calf raise exercise, side view"),
    # 有氧/核心
    ("步行", "brisk-walk.jpg",
     "professional fitness person brisk walking outdoors, athletic clothing, demonstrating proper brisk walking form, front side view"),
    ("核心训练", "core-workout.jpg",
     "fitness coach doing core exercise demonstration, showing abdominal workout position, professional fitness training, demonstrating core strength exercise"),
    ("低冲击有氧", "low-impact-cardio.jpg",
     "professional fitness person doing low impact cardio exercise indoors, gentle movements, showing proper low impact aerobic exercise form"),
    ("拉伸", "stretch.jpg",
     "fitness instructor doing full body dynamic stretch exercise, demonstrating proper stretching form, flexibility training side view"),
    ("全身哑铃循环", "fullbody-dumbbell.jpg",
     "professional fitness coach doing full body dumbbell circuit training, holding dumbbells standing position, demonstrating compound exercise movement front view"),
    ("靠墙静蹲", "wall-sit.jpg",
     "fitness person doing wall sit exercise, back against wall, knees bent 90 degrees, demonstrating proper wall sit position side view"),
    ("泡沫轴放松", "foam-roller.jpg",
     "fitness coach using foam roller for back muscle relaxation, lying on foam roller, demonstrating myofascial release massage, side view"),
    ("平板支撑", "plank.jpg",
     "professional fitness instructor doing plank exercise, forearms and toes supporting body in straight line, demonstrating proper plank form side view"),
    ("卷腹", "crunch.jpg",
     "fitness coach doing abdominal crunch exercise, lying on back curling upper body up, demonstrating proper crunch form, front view"),
    ("墙壁天使", "wall-angel.jpg",
     "fitness person doing wall angel exercise against wall, arms sliding up and down wall like angel wings, demonstrating thoracic mobility exercise, side view"),
    ("肩袖弹力带", "band-external-rotation.jpg",
     "professional fitness coach doing rotator cuff external rotation with resistance band, showing shoulder rehabilitation exercise, front view")
]

def generate_image(action_name, filename, description):
    """生成单张图片"""
    prompt = f"{description}, {STYLE_PREFIX}{STYLE_SUFFIX}"
    
    try:
        print(f"正在生成: {action_name} -> {filename}")
        response = requests.get(API_URL, params={
            "prompt": prompt,
            "image_size": "landscape_4_3"
        }, timeout=120)
        
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'image' in content_type.lower():
                filepath = os.path.join(IMAGE_DIR, filename)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                file_size = os.path.getsize(filepath) / 1024
                print(f"  ✅ 成功保存 ({file_size:.1f} KB)")
                return True
            else:
                print(f"  ⚠️  返回不是图片类型: {content_type}")
                # 尝试解析 JSON 看看返回了什么
                text_preview = response.text[:500]
                print(f"  响应预览: {text_preview}")
                return False
        else:
            print(f"  ❌ HTTP 错误 {response.status_code}")
            return False
            
    except Exception as e:
        print(f"  ❌ 异常: {e}")
        return False

def main():
    print("=" * 60)
    print("开始生成健身动作示范图")
    print(f"共 {len(ACTIONS)} 个动作")
    print("=" * 60)
    print()
    
    success = 0
    failed = []
    
    for i, (name, filename, desc) in enumerate(ACTIONS, 1):
        print(f"\n[{i}/{len(ACTIONS)}] ", end="")
        if generate_image(name, filename, desc):
            success += 1
        else:
            failed.append(name)
        # 间隔避免被限流
        time.sleep(3)
    
    print("\n" + "=" * 60)
    print(f"完成! 成功: {success}/{len(ACTIONS)}")
    if failed:
        print(f"失败: {failed}")
    print("=" * 60)

if __name__ == "__main__":
    main()
