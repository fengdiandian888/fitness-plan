import requests
import os
import time

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

# 统一风格
STYLE = "photorealistic fitness exercise, professional fitness coach, clean white studio background, perfect exercise form, side view showing full body, athletic sportswear, professional lighting, fitness photography, no watermark, high quality sharp focus"

# 需要重新生成的图片（低质量）
ACTIONS = [
    ("dumbbell-bench-press.jpg",
     "dumbbell bench press exercise, fit man lying on bench pressing two dumbbells upward from chest, demonstrating proper chest press form, " + STYLE),
    ("foam-roller.jpg",
     "foam roller exercise for back, person lying on foam roller on floor for myofascial release muscle massage, demonstrating proper foam rolling technique, " + STYLE),
    ("goblet-squat.jpg",
     "goblet squat exercise, fit man holding one dumbbell at chest level, squatting down with knees tracking over toes, demonstrating proper squat form, " + STYLE),
    ("incline-dumbbell-press.jpg",
     "incline dumbbell press exercise on incline bench, upper body slightly elevated, pressing dumbbells upward for upper chest workout, demonstrating proper incline press form, " + STYLE),
    ("lateral-raise.jpg",
     "dumbbell lateral raise exercise, fit man raising dumbbells out to sides like wings until arms parallel to floor, demonstrating proper shoulder lateral raise form, " + STYLE),
    ("plank.jpg",
     "plank exercise, fit person in perfect plank position with forearms and toes supporting body in straight line from head to heels, demonstrating proper core strength exercise, side view, " + STYLE),
    ("rotator-cuff.jpg",
     "wall angel exercise against wall, fit person standing with back against wall, arms sliding up and down wall like wings, demonstrating proper thoracic mobility and shoulder rehabilitation exercise, " + STYLE),
    ("stretch.jpg",
     "full body dynamic stretching exercise, fitness person doing standing hamstring and arm stretch, demonstrating proper flexibility training form, " + STYLE),
    ("tricep-pushdown.jpg",
     "triceps dumbbell kickback exercise, bent over position with one hand on bench, extending arm backward showing triceps muscle contraction, demonstrating proper triceps exercise form, " + STYLE),
]

print("Regenerating " + str(len(ACTIONS)) + " low-quality images...")
print()

success = 0
failed = []

for i, (filename, prompt) in enumerate(ACTIONS, 1):
    try:
        print("[" + str(i) + "/" + str(len(ACTIONS)) + "] Generating: " + filename)
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
                if size_kb > 20:
                    print("  OK - " + str(round(size_kb, 1)) + " KB")
                    success += 1
                else:
                    print("  STILL LOW - " + str(round(size_kb, 1)) + " KB")
                    failed.append(filename)
            else:
                print("  FAILED - not image, got: " + content_type)
                failed.append(filename)
        else:
            print("  FAILED - HTTP " + str(response.status_code))
            failed.append(filename)
    except Exception as e:
        print("  FAILED - " + str(e))
        failed.append(filename)
    
    time.sleep(5)

print()
print("Done. Success: " + str(success) + "/" + str(len(ACTIONS)))
if failed:
    print("Issues: " + ", ".join(failed))
