from PIL import Image
import requests
import shutil
import getlinks
import time

link = "https://media.vidigami.com/media/production_images_32699338/dyn/max_D/4672-4672"
cookies = {'production-global-vidigami': 'fa135f43eb7550938a60754957c88c1d9c0231fff97315d3e2cb8223726fef09'}

links = getlinks.getlinks()
links.reverse()

# img_data = requests.get(link, cookies=cookies).content
# with open("test", 'wb') as handler:
#     handler.write(img_data)

cnt = 1

while len(links) > 0:

    url = links.pop()
    print(url)

    try:

        img_data = requests.get(url, cookies=cookies, timeout=5).content
        print('get done')
        with open(str(cnt) + ".png", 'wb') as handler:
            handler.write(img_data)
        cnt += 1
    except:
        print("timeout")
        links.append(url)

        
    time.sleep(1)