import os

save_dir = r'd:\solo\images'
files = os.listdir(save_dir)
jpg_files = sorted([f for f in files if f.endswith('.jpg')])

print(f'images 目录: {len(jpg_files)} 个 JPG 文件')
print()
print('文件名 -> 文件大小')
print('-' * 50)
for f in jpg_files:
    size = os.path.getsize(os.path.join(save_dir, f))
    size_kb = size // 1024
    print(f'{f:35s} {size_kb:5d} KB')
