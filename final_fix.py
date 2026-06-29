import requests
import os
import sys

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

def generate_one(filename, prompt):
    filepath = os.path.join(IMAGE_DIR, filename)
    print("Generating " + filename + "...")
    sys.stdout.flush()

    for attempt in range(5):
        try:
            response = requests.get(API_URL, params={
                "prompt": prompt,
                "image_size": "landscape_4_3"
            }, timeout=300)

            if response.status_code == 200:
                content_type = response.headers.get("content-type", "")
                data = response.content
                if "image" in content_type.lower() and len(data) > 50000:
                    if len(data) > 2 and data[0] == 0xFF and data[1] == 0xD8:
                        with open(filepath, "wb") as f:
                            f.write(data)
                        print("  OK! " + str(len(data)) + " bytes, JPEG confirmed")
                        sys.stdout.flush()
                        return True
                    else:
                        print("  got image but not JPEG, retrying...")
                        sys.stdout.flush()
                else:
                    print("  content too small or wrong type: " + content_type + ", " + str(len(data)) + " bytes")
                    sys.stdout.flush()
            else:
                print("  HTTP " + str(response.status_code) + ", retrying...")
                sys.stdout.flush()
        except Exception as e:
            print("  Exception: " + str(e) + ", retrying...")
            sys.stdout.flush()
        import time
        time.sleep(10)

    print("  FAILED: " + filename)
    sys.stdout.flush()
    return False

# 逐个生成
generate_one("brisk-walk.jpg",
    "professional fitness person doing brisk walking exercise, athletic person walking with good posture outdoors, fitness lifestyle, side view, photorealistic, clean background, professional lighting")

import time
time.sleep(5)

generate_one("core-workout.jpg",
    "professional fitness coach demonstrating core strength training, fit person doing abdominal workout on exercise mat, proper form, clean white studio background, side view, photorealistic, professional lighting")

time.sleep(5)

generate_one("low-impact-cardio.jpg",
    "professional fitness person doing low impact cardio exercise indoors, gentle aerobic movements without jumping, mild aerobic training, clean studio gym background, side view, photorealistic")

time.sleep(5)

generate_one("fullbody-dumbbell.jpg",
    "professional fitness coach doing full body dumbbell compound exercise, standing position holding dumbbells, demonstrating proper full body workout form, side view, clean white studio background, photorealistic")

time.sleep(5)

generate_one("wall-sit.jpg",
    "professional fitness coach doing wall sit exercise, back flat against wall, knees bent 90 degrees, thighs parallel to floor, demonstrating proper wall sit position, side view, clean white studio background, photorealistic")

time.sleep(5)

generate_one("crunch.jpg",
    "professional fitness instructor doing abdominal crunch exercise, lying on back curling upper body up toward knees, demonstrating proper crunch form, core strength training, side view, clean white studio background, photorealistic")

print()
print("ALL DONE")
