import os

images_dir = r'd:\solo\images'
files = sorted(os.listdir(images_dir))

print('图片文件检查（按大小排序）：')
print('=' * 70)

file_sizes = []
for f in files:
    if f.endswith('.jpg'):
        path = os.path.join(images_dir, f)
        size = os.path.getsize(path)
        file_sizes.append((f, size))

file_sizes.sort(key=lambda x: x[1])

for f, size in file_sizes:
    kb = size / 1024
    # 小文件可能是无效的占位图
    if size < 5000:
        status = '无效(<5KB)'
    elif size < 20000:
        status = '小(<20KB)'
    else:
        status = '正常'
    print(f'{f:35s} {kb:8.1f} KB  {status}')

print()
print('=' * 70)
print(f'共 {len(file_sizes)} 个文件')
small_count = sum(1 for _, s in file_sizes if s < 20000)
print(f'<20KB 的文件: {small_count} 个 - 可能是无效占位图')
print(f'>20KB 的文件: {len(file_sizes) - small_count} 个 - 可能是有效图片')
