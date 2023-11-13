from PIL import Image
import requests
import shutil
import getlinks
import time

link = "https://media.vidigami.com/media/production_images_32699338/dyn/max_D/2560-2560"
cookies = {'production-global-vidigami': 'edb6c25d77a33325a48bdcd5dee8c7cbd74e53f51ff6c2d3a2b5c599e4b653d5'}

links = getlinks.getlinks()

# img_data = requests.get(link, cookies=cookies).content
# with open("test", 'wb') as handler:
#     handler.write(img_data)

cnt = 1
for url in links:
    print(url)

    img_data = requests.get(url, cookies=cookies).content
    with open(str(cnt) + ".png", 'wb') as handler:
        handler.write(img_data)

    cnt += 1
    time.sleep(0.1)
