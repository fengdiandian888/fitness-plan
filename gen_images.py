import requests
import os
import time

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

# 统一风格描述词
STYLE = "photorealistic fitness exercise demonstration, professional fitness coach, clean white studio background, perfect exercise form, side view showing full body, athletic sportswear, professional lighting, fitness photography, no watermark, high quality"

# 动作清单（图片文件名需与 data.js 中的 image 字段保持一致）
ACTIONS = [
    # 拉日
    ("bent-over-row.jpg",
     "dumbbell bent-over row exercise, man holding dumbbells, torso bent forward 45 degrees, back straight pulling dumbbells to waist level, demonstrating proper rowing form, " + STYLE),
    ("cable-pulldown.jpg",
     "resistance band lat pulldown exercise, pulling band down from overhead to chest, back straight, demonstrating proper lat pulldown form, " + STYLE),
    ("band-external-rotation.jpg",
     "resistance band external rotation exercise, shoulder rehabilitation, arm at side elbow 90 degrees rotating outward, demonstrating proper rotator cuff exercise, " + STYLE),
    ("deadlift.jpg",
     "dumbbell deadlift exercise, standing position holding dumbbells, back straight, hips back, demonstrating proper deadlift form, " + STYLE),
    ("bicep-curl.jpg",
     "dumbbell bicep curl exercise, alternating curl, arms curling dumbbells up toward shoulders, demonstrating proper bicep curl form, " + STYLE),
    # 推日
    ("dumbbell-bench-press.jpg",
     "dumbbell bench press exercise, man lying on bench pressing dumbbells upward from chest, demonstrating proper chest press form, " + STYLE),
    ("incline-dumbbell-press.jpg",
     "incline dumbbell press exercise, upper body on incline bench, pressing dumbbells upward, upper chest exercise, " + STYLE),
    ("lateral-raise.jpg",
     "dumbbell lateral raise exercise, arms raising dumbbells out to sides like wings, shoulder exercise, demonstrating proper lateral raise form, " + STYLE),
    ("tricep-pushdown.jpg",
     "triceps dumbbell kickback exercise, bent over position, extending arm backward showing triceps, demonstrating proper triceps exercise form, " + STYLE),
    ("rotator-cuff.jpg",
     "wall angel exercise against wall, arms sliding up and down wall like wings, demonstrating thoracic mobility exercise, " + STYLE),
    # 腿日
    ("goblet-squat.jpg",
     "goblet squat exercise, holding one dumbbell at chest level, squatting down with knees tracking over toes, demonstrating proper squat form, " + STYLE),
    ("split-squat.jpg",
     "bulgarian split squat exercise, back foot elevated on bench, front leg in lunging position, demonstrating proper single leg squat form, " + STYLE),
    ("single-leg-rdl.jpg",
     "romanian deadlift exercise with dumbbells, keeping legs straight slightly bent, hinging at hips lowering dumbbells to shins, hamstring and glute activation, " + STYLE),
    ("single-leg-glute-bridge.jpg",
     "single leg glute bridge exercise on floor, one leg extended, hips lifting up off floor, demonstrating proper glute bridge form, " + STYLE),
    ("calf-raise.jpg",
     "standing calf raise exercise, elevating heels by standing on toes, demonstrating proper calf raise exercise form, " + STYLE),
    # 有氧/核心
    ("brisk-walk.jpg",
     "brisk walking exercise outdoors, athletic person walking with good posture, demonstrating proper brisk walking form, " + STYLE),
    ("core-workout.jpg",
     "core strength training exercise demonstration, fitness person doing abdominal workout on floor, demonstrating proper core exercise form, " + STYLE),
    ("low-impact-cardio.jpg",
     "low impact cardio exercise indoors, gentle aerobic movements without jumping, demonstrating proper low impact exercise, " + STYLE),
    ("stretch.jpg",
     "full body dynamic stretching exercise, fitness person doing arm and leg stretches, demonstrating proper flexibility training form, " + STYLE),
    ("fullbody-dumbbell.jpg",
     "full body dumbbell circuit training, holding dumbbells standing position, compound exercise movement demonstration, " + STYLE),
    ("wall-sit.jpg",
     "wall sit exercise, back flat against wall, knees bent 90 degrees, thighs parallel to floor, demonstrating proper wall sit position, " + STYLE),
    ("foam-roller.jpg",
     "foam roller myofascial release exercise, person lying on foam roller for back muscle relaxation and massage, demonstrating proper foam rolling, " + STYLE),
    ("plank.jpg",
     "plank exercise, forearms and toes supporting body in perfectly straight line from head to heels, demonstrating proper plank form, side view, " + STYLE),
    ("crunch.jpg",
     "abdominal crunch exercise, lying on back, curling upper body up toward knees, demonstrating proper crunch form, " + STYLE),
]

def generate_one(filename, prompt):
    try:
        print("  Generating: " + filename)
        response = requests.get(API_URL, params={
            "prompt": prompt,
            "image_size": "landscape_4_3"
        }, timeout=180)
        
        if response.status_code == 200:
            content_type = response.headers.get("content-type", "")
            if "image" in content_type.lower():
                filepath = os.path.join(IMAGE_DIR, filename)
                with open(filepath, "wb") as f:
                    f.write(response.content)
                size_kb = os.path.getsize(filepath) / 1024
                print("  OK - " + str(round(size_kb, 1)) + " KB")
                return True
            else:
                print("  FAILED - not an image, got: " + content_type)
                return False
        else:
            print("  FAILED - HTTP " + str(response.status_code))
            return False
    except Exception as e:
        print("  FAILED - " + str(e))
        return False

def main():
    print("=" * 60)
    print("Starting fitness exercise image generation")
    print("Total: " + str(len(ACTIONS)) + " exercises")
    print("=" * 60)
    print()
    
    success = 0
    failed = []
    
    for i, (filename, prompt) in enumerate(ACTIONS, 1):
        print("[" + str(i) + "/" + str(len(ACTIONS)) + "] ", end="")
        if generate_one(filename, prompt):
            success += 1
        else:
            failed.append(filename)
        time.sleep(4)  # 间隔避免限流
    
    print()
    print("=" * 60)
    print("Done! Success: " + str(success) + "/" + str(len(ACTIONS)))
    if failed:
        print("Failed: " + ", ".join(failed))
    print("=" * 60)

if __name__ == "__main__":
    main()
