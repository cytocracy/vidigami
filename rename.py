#rename all files in folder from .png to .jpg
import os
path = './test/'
print(path)
files = os.listdir(path)
print(files)
for file in files:
    if file.endswith(".png"):
        os.rename(file, file[:-4] + ".jpg")

# Path: image.py