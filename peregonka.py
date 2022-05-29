import json

from PIL import Image
import os

for filename in os.listdir("dataset/images/valid"):
    im = Image.open(f"dataset/images/valid/{filename}")
    l = len(filename)
    filejs = filename[:l-3]
    with open(f"yolov5/dataset/markup/{filejs}json") as json_file:
        (width, height) = im.size
        data = json.load(json_file)
        file = open(f"dataset/labels/valid/{filejs}txt", "w")
        for p in data:
            k=0

            for i in p["bbox"]:
                if k == 0:
                    file.write("0")
                    file.write(" ")
                k+=1
                if k==1 or k==3:
                  file.write(str(i/width))
                if k ==2 or k==4:
                    file.write(str(i/height))
                    file.write(" ")
                if k == 4:
                    file.write('\n')
                    k=0
            file.close()
# data[]