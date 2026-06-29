import os

IMAGE_DIR = r"d:\solo\images"

images = [
    'bent-over-row.jpg', 'bicep-curl.jpg', 'cable-pulldown.jpg',
    'band-external-rotation.jpg', 'deadlift.jpg', 'dumbbell-bench-press.jpg',
    'incline-dumbbell-press.jpg', 'lateral-raise.jpg', 'tricep-pushdown.jpg',
    'rotator-cuff.jpg', 'goblet-squat.jpg', 'split-squat.jpg',
    'single-leg-rdl.jpg', 'single-leg-glute-bridge.jpg', 'calf-raise.jpg',
    'brisk-walk.jpg', 'core-workout.jpg', 'low-impact-cardio.jpg',
    'stretch.jpg', 'fullbody-dumbbell.jpg', 'wall-sit.jpg', 'foam-roller.jpg',
    'plank.jpg', 'crunch.jpg'
]

print("Checking image files:")
print()
for img in images:
    filepath = os.path.join(IMAGE_DIR, img)
    if os.path.exists(filepath):
        size = os.path.getsize(filepath)
        # 读取前几个字节检查是否是 JPEG
        with open(filepath, 'rb') as f:
            header = f.read(4)
        # JPEG 以 FF D8 开头
        is_jpeg = header[0] == 0xFF and header[1] == 0xD8
        status = "OK (JPEG)" if is_jpeg else "UNKNOWN FORMAT"
        print("  " + img.ljust(32) + " -> " + str(size).rjust(8) + " bytes, " + status)
    else:
        print("  " + img.ljust(32) + " -> MISSING")
