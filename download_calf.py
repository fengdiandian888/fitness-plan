import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urls = {
    'calf-raise.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Calf-raise-1.png/640px-Calf-raise-1.png',
}

save_dir = r'd:\solo\images'

for filename, url in urls.items():
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        })
        data = urllib.request.urlopen(req, timeout=60).read()
        if len(data) > 1000:
            filepath = save_dir + '\\' + filename
            with open(filepath, 'wb') as f:
                f.write(data)
            print(f'{filename}: {len(data)//1024} KB - OK')
        else:
            print(f'{filename}: 文件太小 ({len(data)}字节)')
    except Exception as e:
        print(f'{filename}: 失败 - {str(e)[:80]}')

print('完成')
