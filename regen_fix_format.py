import requests
import os
import time

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

ACTIONS = [
    ("bicep-curl.jpg",
     "dumbbell bicep curl exercise, man standing curling dumbbells up toward shoulders, demonstrating proper bicep curl form side view, professional fitness coaching, clean white background"),
    ("deadlift.jpg",
     "dumbbell deadlift exercise, man standing holding dumbbells, back straight hips back, demonstrating proper deadlift starting position side view, professional fitness coaching, white background"),
    ("split-squat.jpg",
     "bulgarian split squat exercise, back foot elevated on bench, front leg lunging, demonstrating proper single leg squat form side view, professional fitness training, white background"),
    ("single-leg-rdl.jpg",
     "romanian deadlift with dumbbells, man hinging at hips lowering dumbbells to shins, hamstring and glute activation, demonstrating proper romanian deadlift form side view, professional fitness, white background"),
    ("single-leg-glute-bridge.jpg",
     "single leg glute bridge exercise on floor, one leg extended, hips lifting up off ground, demonstrating proper glute bridge form, professional fitness training side view, white background"),
    ("calf-raise.jpg",
     "standing calf raise exercise, person elevating heels by standing on toes, demonstrating proper calf raise exercise form side view, professional fitness training, white background"),
    ("brisk-walk.jpg",
     "brisk walking exercise outdoors, athletic person walking with good posture, demonstrating proper brisk walking form, professional fitness lifestyle photo, outdoor background"),
    ("core-workout.jpg",
     "core strength training exercise, fit person doing abdominal workout on floor in plank position variation, demonstrating proper core exercise form, professional fitness training, white background"),
    ("low-impact-cardio.jpg",
     "low impact cardio exercise indoors, gentle aerobic movements without jumping, person doing mild aerobic training, professional fitness lifestyle, indoor gym background"),
    ("fullbody-dumbbell.jpg",
     "full body dumbbell circuit training, fit person standing holding dumbbells ready for compound exercise movements, demonstrating proper full body workout form, professional fitness, white background"),
    ("wall-sit.jpg",
     "wall sit exercise, person with back flat against wall, knees bent 90 degrees, thighs parallel to floor, demonstrating proper wall sit position side view, professional fitness, white background"),
    ("crunch.jpg",
     "abdominal crunch exercise, person lying on back curling upper body up toward knees, demonstrating proper crunch form, professional core strength training side view, white background")
]

print("Regenerating " + str(len(ACTIONS)) + " images (fixing file format)...")
print()

success = 0
failed = []
for i, (filename, prompt) in enumerate(ACTIONS, 1):
    for attempt in range(3):
        try:
            print("[" + str(i) + "/" + str(len(ACTIONS)) + "] Generating: " + filename + " (attempt " + str(attempt + 1) + ")")
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
                    # Verify it's actually JPEG
                    with open(filepath, "rb") as f:
                        header = f.read(2)
                    if header[0] == 0xFF and header[1] == 0xD8:
                        print("  OK - " + str(round(size_kb, 1)) + " KB, real JPEG")
                        success += 1
                        break
                    else:
                        print("  Still wrong format, retrying...")
                else:
                    print("  Not image: " + content_type + ", retrying...")
            else:
                print("  HTTP " + str(response.status_code) + ", retrying...")
        except Exception as e:
            print("  Error: " + str(e) + ", retrying...")
        time.sleep(5)
    else:
        failed.append(filename)
        print("  FAILED after 3 attempts")
    time.sleep(3)

print()
print("=" * 50)
print("SUCCESS: " + str(success) + "/" + str(len(ACTIONS)))
if failed:
    print("FAILED: " + ", ".join(failed))
print("=" * 50)
