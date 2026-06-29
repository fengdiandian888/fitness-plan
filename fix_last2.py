import requests
import os
import time

API_URL = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
IMAGE_DIR = r"d:\solo\images"

files = [
    ("wall-sit.jpg",
     "professional fitness coach doing wall sit exercise, back flat against wall, knees bent 90 degrees, demonstrating proper wall sit position, side view, clean white studio background, photorealistic, professional lighting"),
    ("crunch.jpg",
     "professional fitness instructor doing abdominal crunch exercise, person lying on back curling upper body up toward knees, demonstrating proper crunch form, core strength training, side view, clean white studio background, photorealistic, professional lighting")
]

for filename, prompt in files:
    filepath = os.path.join(IMAGE_DIR, filename)
    old_size = os.path.getsize(filepath)
    print("Updating " + filename + " (old: " + str(old_size) + " bytes)")

    for attempt in range(5):
        try:
            print("  attempt " + str(attempt + 1) + "...", end=" ")
            response = requests.get(API_URL, params={"prompt": prompt, "image_size": "landscape_4_3"}, timeout=300)
            if response.status_code == 200:
                data = response.content
                ct = response.headers.get("content-type", "")
                if "image" in ct.lower() and len(data) > 50000:
                    if data[0] == 0xFF and data[1] == 0xD8:
                        with open(filepath, "wb") as f:
                            f.write(data)
                        print("OK! " + str(len(data)) + " bytes")
                        break
                    else:
                        print("not JPEG format")
                else:
                    print("too small / wrong type: " + ct + ", " + str(len(data)) + " bytes")
            else:
                print("HTTP " + str(response.status_code))
        except Exception as e:
            print("Exception: " + str(e))
        time.sleep(15)
    time.sleep(10)

print("DONE")
