import requests
import os
import time

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

# 简化的 prompt，避免太长导致问题
ACTIONS = [
    ("goblet-squat.jpg",
     "fitness man doing goblet squat holding dumbbell at chest, proper squat form, white studio background, photorealistic"),
    ("incline-dumbbell-press.jpg",
     "fitness man doing incline dumbbell press on bench, pressing dumbbells up, upper chest exercise, white studio background, photorealistic"),
    ("lateral-raise.jpg",
     "fitness man doing dumbbell lateral raise, arms raising dumbbells out to sides like wings, shoulder exercise, white studio background, photorealistic"),
    ("plank.jpg",
     "fitness person doing plank exercise, forearms and toes supporting body in perfect straight line, core strength training, side view, white studio background, photorealistic"),
    ("rotator-cuff.jpg",
     "fitness person doing wall angel exercise against wall, arms sliding up and down wall like wings, shoulder mobility training, side view, white studio background, photorealistic"),
    ("stretch.jpg",
     "fitness person doing full body stretching exercises, arm and leg stretches, flexibility training, white studio background, photorealistic"),
    ("tricep-pushdown.jpg",
     "fitness man doing triceps dumbbell kickback exercise, bent over position, extending arm backward showing triceps, white studio background, photorealistic"),
]

def try_generate(filename, prompt, max_attempts=3):
    for attempt in range(max_attempts):
        try:
            print("  Attempt " + str(attempt + 1) + ": " + filename)
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
                    if size_kb > 50:  # 大于 50KB 通常是正常图片
                        print("  SUCCESS - " + str(round(size_kb, 1)) + " KB")
                        return True
                    else:
                        print("  Too small: " + str(round(size_kb, 1)) + " KB, retrying...")
                else:
                    print("  Not image: " + content_type + ", retrying...")
            else:
                print("  HTTP " + str(response.status_code) + ", retrying...")
        except Exception as e:
            print("  Error: " + str(e) + ", retrying...")
        
        time.sleep(6)
    
    print("  FAILED after " + str(max_attempts) + " attempts")
    return False

print("Regenerating " + str(len(ACTIONS)) + " images with retry...")
print()

success = 0
failed = []
for i, (filename, prompt) in enumerate(ACTIONS, 1):
    print("[" + str(i) + "/" + str(len(ACTIONS)) + "]")
    if try_generate(filename, prompt):
        success += 1
    else:
        failed.append(filename)
    print()

print("=" * 50)
print("Total: " + str(success) + "/" + str(len(ACTIONS)))
if failed:
    print("Still failed: " + ", ".join(failed))
