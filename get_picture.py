import requests
import os

url = "http://img1.cache.netease.com/catchpic/8/88/88F4DEC501D671103282BCA21918B247.jpg"
cur_dir = os.curdir
root = cur_dir + "/Download/"
path = root + url.split('/')[-1]
print("Save to:" + path)

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("File saved successfully")
    else:
        print("File already exists")
except:
    print("Failed in getting the picture")
