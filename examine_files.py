import os

IMAGE_DIR = r"d:\solo\images"

images = [
    'brisk-walk.jpg', 'core-workout.jpg', 'low-impact-cardio.jpg',
    'fullbody-dumbbell.jpg', 'wall-sit.jpg', 'crunch.jpg'
]

print("Checking remaining 6 files:")
print()
for img in images:
    filepath = os.path.join(IMAGE_DIR, img)
    size = os.path.getsize(filepath)
    with open(filepath, 'rb') as f:
        header = f.read(64)

    # Show first bytes as hex and as text
    hex_str = ' '.join('{:02x}'.format(b) for b in header[:20])
    try:
        text_str = header[:60].decode('utf-8', errors='replace')
    except:
        text_str = "unreadable"

    print(img + " (" + str(size) + " bytes):")
    print("  HEX:  " + hex_str)
    print("  TEXT: " + text_str[:100])
    print()
