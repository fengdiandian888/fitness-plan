import re
import os

data_js = open(r"d:\solo\data.js", "r", encoding="utf-8").read()

# 提取所有 image: 'xxx.jpg'
matches = re.findall(r'image:\s*"([^"]+)"', data_js)
# 也检查单引号
matches += re.findall(r"image:\s*'([^']+)'", data_js)

# 去重
unique_images = list(set(matches))
unique_images.sort()

print("data.js 中引用的图片:")
print()

image_dir = r"d:\solo\images"
status = []
for img in unique_images:
    filepath = os.path.join(image_dir, img)
    if os.path.exists(filepath):
        size_kb = os.path.getsize(filepath) / 1024
        if size_kb < 20:
            s = "LOW QUALITY (可能是占位图)"
        else:
            s = "OK"
        status.append((img, size_kb, s))
    else:
        status.append((img, 0, "MISSING"))

# 打印
max_len = max(len(x[0]) for x in status)
for img, size, s in status:
    if size > 0:
        print("  " + img.ljust(max_len + 4) + " -> " + str(round(size, 1)) + " KB  " + s)
    else:
        print("  " + img.ljust(max_len + 4) + " -> MISSING")

print()
print("总计: " + str(len(status)) + " 个图片")
print("OK: " + str(sum(1 for x in status if x[2] == "OK")))
print("LOW QUALITY: " + str(sum(1 for x in status if x[2] == "LOW QUALITY (可能是占位图)")))
print("MISSING: " + str(sum(1 for x in status if x[2] == "MISSING")))
