import os

IMAGE_DIR = r"d:\solo\images"

images = [
    'bicep-curl.jpg', 'deadlift.jpg', 'split-squat.jpg',
    'single-leg-rdl.jpg', 'single-leg-glute-bridge.jpg', 'calf-raise.jpg',
    'brisk-walk.jpg', 'core-workout.jpg', 'low-impact-cardio.jpg',
    'fullbody-dumbbell.jpg', 'wall-sit.jpg', 'crunch.jpg'
]

print("Checking UNKNOWN format files:")
print()
for img in images:
    filepath = os.path.join(IMAGE_DIR, img)
    with open(filepath, 'rb') as f:
        header = f.read(16)
    
    # 检查各种格式的 magic bytes
    if header[0] == 0xFF and header[1] == 0xD8:
        fmt = "JPEG"
    elif header[0] == 0x89 and header[1:4] == b'PNG':
        fmt = "PNG (file extension mismatch!)"
    elif header[0:3] == b'GIF':
        fmt = "GIF"
    elif header[0:4] == b'RIFF' and header[8:12] == b'WEBP':
        fmt = "WEBP"
    else:
        hex_values = ' '.join('{:02x}'.format(b) for b in header)
        fmt = "UNKNOWN - header bytes: " + hex_values
    
    print("  " + img + ": " + fmt)
