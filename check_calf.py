import os
path = r'd:\solo\images\calf-raise.jpg'
if os.path.exists(path):
    print('calf-raise.jpg 存在:', os.path.getsize(path) // 1024, 'KB')
else:
    print('calf-raise.jpg 不存在')
    print('images 目录文件:', sorted(os.listdir(r'd:\solo\images'))[:5])
