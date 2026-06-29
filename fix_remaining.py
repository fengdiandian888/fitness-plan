import requests
import os
import time

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

# 剩余需要修复的图片
NEED_FIX = [
    ("single-leg-rdl.jpg",
     "professional fitness instructor demonstrating dumbbell romanian deadlift exercise, standing position holding dumbbells hinging at hips, hamstring and glute activation, side view, clean white studio background, professional lighting, photorealistic"),
    ("single-leg-glute-bridge.jpg",
     "professional fitness coach doing single leg glute bridge exercise on floor, one leg extended, hips lifting up off ground, demonstrating proper glute bridge form, side view, white studio background, photorealistic"),
    ("calf-raise.jpg",
     "professional fitness person doing standing calf raise exercise, elevating heels by standing on toes, demonstrating proper calf raise exercise form, side view, clean white studio background, photorealistic"),
    ("brisk-walk.jpg",
     "professional fitness person doing brisk walking exercise outdoors, athletic clothing, proper walking posture, fitness lifestyle photography, clean background, photorealistic"),
    ("core-workout.jpg",
     "professional fitness coach demonstrating core strength training exercise, person doing abdominal workout on exercise mat, core engagement, proper form, clean white studio background, photorealistic"),
    ("low-impact-cardio.jpg",
     "professional fitness person doing low impact cardio exercise indoors, gentle aerobic movements without jumping, mild aerobic training, clean studio background, photorealistic"),
    ("fullbody-dumbbell.jpg",
     "professional fitness coach doing full body dumbbell compound exercise, standing position holding dumbbells ready for full body workout, demonstrating proper form, clean white studio background, photorealistic"),
    ("wall-sit.jpg",
     "professional fitness coach doing wall sit exercise, back flat against wall, knees bent 90 degrees, thighs parallel to floor, demonstrating proper wall sit position, side view, clean white studio background, photorealistic"),
    ("crunch.jpg",
     "professional fitness instructor doing abdominal crunch exercise, lying on back curling upper body up toward knees, demonstrating proper crunch form, core strength training, side view, clean white studio background, photorealistic")
]

print("Fixing " + str(len(NEED_FIX)) + " images...")
print()

for i, (filename, prompt) in enumerate(NEED_FIX, 1):
    filepath = os.path.join(IMAGE_DIR, filename)
    old_size = os.path.getsize(filepath) if os.path.exists(filepath) else 0
    print("[" + str(i) + "/" + str(len(NEED_FIX)) + "] " + filename + " (old: " + str(old_size) + " bytes)")

    success = False
    for attempt in range(5):
        try:
            print("  attempt " + str(attempt + 1) + "...", end=" ")
            response = requests.get(API_URL, params={
                "prompt": prompt,
                "image_size": "landscape_4_3"
            }, timeout=240)

            if response.status_code == 200:
                content_type = response.headers.get("content-type", "")
                if "image" in content_type.lower():
                    data = response.content
                    # Verify JPEG header
                    if len(data) > 2 and data[0] == 0xFF and data[1] == 0xD8:
                        with open(filepath, "wb") as f:
                            f.write(data)
                        new_size = os.path.getsize(filepath)
                        print("OK - " + str(new_size) + " bytes (JPEG confirmed)")
                        success = True
                        break
                    else:
                        print("wrong format")
                else:
                    print("not image: " + content_type)
            else:
                print("HTTP " + str(response.status_code))
        except Exception as e:
            print("error: " + str(e))
        time.sleep(8)

    if not success:
        print("  FAILED to fix " + filename)
    time.sleep(4)

print()
print("DONE - check with check_image_format.py")
