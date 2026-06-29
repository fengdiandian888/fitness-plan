import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

save_dir = r'd:\solo\images'

# 用确定能工作的URL（前面测试确认可用）下载剩余动作
# 用同一个稳定源的不同图片ID
urls = [
    # 用测试确认可用的URL下载这些动作
    ('03-band-external-rotation.jpg', 'https://aka.doubaocdn.com/s/kwvY1wfTUF'),  # 弹力带动作
    ('04-romanian-deadlift.jpg', 'https://aka.doubaocdn.com/s/ppvR1wfTUF'),         # 硬拉动作
    ('05-dumbbell-bench-press.jpg', 'https://aka.doubaocdn.com/s/yBkY1wfTUF'),    # 卧推/推
    ('06-shoulder-press.jpg', 'https://aka.doubaocdn.com/s/06vR1wfTUF'),          # 肩推
    ('07-lateral-raise.jpg', 'https://aka.doubaocdn.com/s/hZ3Y1wfTUF'),           # 侧平举
    ('08-tricep-exercise.jpg', 'https://aka.doubaocdn.com/s/49mY1wfTUF'),         # 三头肌动作
    ('13-plank-core.jpg', 'https://aka.doubaocdn.com/s/3V2Y1wfTUF'),              # 平板/核心
    ('14-resistance-band.jpg', 'https://aka.doubaocdn.com/s/yYVY1wfTUF'),         # 弹力带
]

for filename, url in urls:
    filepath = f'{save_dir}\\{filename}'
    try:
        urllib.request.urlretrieve(url, filepath)
        import os
        size = os.path.getsize(filepath)
        if size > 1000:  # 大于1KB算有效
            print(f'OK  {filename}  ({size} bytes)')
        else:
            print(f'SMALL {filename} ({size} bytes) - may be error page')
    except Exception as e:
        print(f'FAIL {filename}: {e}')

print('\n完成')
