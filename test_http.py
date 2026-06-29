import urllib.request

urls = [
    'http://localhost:8000/images/bent-over-row.jpg',
    'http://localhost:8000/images/plank.jpg',
    'http://localhost:8000/images/goblet-squat.jpg'
]
for url in urls:
    try:
        r = urllib.request.urlopen(url, timeout=10)
        data = r.read()
        print(url + " -> " + str(len(data)) + " bytes")
    except Exception as e:
        print(url + " -> ERROR: " + str(e))

print()
print("Done")
