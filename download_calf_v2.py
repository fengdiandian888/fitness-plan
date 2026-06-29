import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 多个备用 URL
urls_to_try = [
    ('calf-raise.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Calf-raise-1.png/640px-Calf-raise-1.png'),
    ('calf-raise.jpg', 'https://aka.doubaocdn.com/s/erCd1wfTOF'),
]

save_dir = r'd:\solo\images'

for filename, url in urls_to_try:
    try:
        print(f'尝试: {url[:60]}...')
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        })
        data = urllib.request.urlopen(req, timeout=30).read()
        if len(data) > 1000:
            filepath = save_dir + '\\' + filename
            with open(filepath, 'wb') as f:
                f.write(data)
            print(f'成功: {len(data)//1024} KB')
            break
        else:
            print(f'跳过: 文件太小 ({len(data)}字节)')
    except Exception as e:
        print(f'失败: {str(e)[:60]}')

print('完成')
