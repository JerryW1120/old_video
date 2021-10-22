import os


dir = "/Users/jerryw/Desktop/文档/老电影修复/dpx文件/"
directory = os.listdir(dir)

for file in directory:
    
    if str(file).split(".")[-1] == "dpx":
        os.popen(f'ffmpeg -i {dir}{file} {dir}{str(file).split(".")[0]}.png')