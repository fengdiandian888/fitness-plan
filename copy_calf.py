import shutil
import os

# 用已有的 split-squat.jpg 或 wall-sit.jpg 作为 calf-raise.jpg（都是下肢动作）
source = r'd:\solo\images\wall-sit.jpg'
target = r'd:\solo\images\calf-raise.jpg'

if os.path.exists(source):
    shutil.copy(source, target)
    print(f'已复制 wall-sit.jpg -> calf-raise.jpg')
    print(f'文件大小: {os.path.getsize(target)//1024} KB')
else:
    # 尝试另一个
    source2 = r'd:\solo\images\split-squat.jpg'
    if os.path.exists(source2):
        shutil.copy(source2, target)
        print(f'已复制 split-squat.jpg -> calf-raise.jpg')
    else:
        print('没有合适的源图片')
