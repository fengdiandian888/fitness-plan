import requests
import os

url = "https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image"
print("测试图片生成 API...")

prompt = "professional fitness coach doing dumbbell bent-over row, man holding dumbbells, torso bent forward, back straight pulling dumbbells to hips, photorealistic, clean white studio background, side view full body, professional lighting, 4k, fitness photography, no watermark"

try:
    response = requests.get(url, params={
        "prompt": prompt,
        "image_size": "landscape_4_3"
    }, timeout=120)
    
    print("HTTP status: " + str(response.status_code))
    content_type = response.headers.get("content-type", "")
    print("Content-Type: " + content_type)
    
    if response.status_code == 200 and "image" in content_type.lower():
        filepath = r"d:\solo\images\test-row.jpg"
        with open(filepath, "wb") as f:
            f.write(response.content)
        size = os.path.getsize(filepath) / 1024
        print("Image saved, size: " + str(round(size, 1)) + " KB")
        print("SUCCESS")
    else:
        print("Response preview:")
        print(response.text[:800])
except Exception as e:
    print("Error: " + str(e))
