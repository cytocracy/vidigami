import time

def getlinks():

    links   = []
    f = open('nums.txt', 'r')
    for line in f:
        link = "https://media.vidigami.com/media/production_images_" + line.strip() + "/dyn/max_D/4672-4672"
        # print(link)
        links.append(link)

    return links

if __name__ == "__main__":
    getlinks()