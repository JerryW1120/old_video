import os
dir = "D:\原始2分场景"

folders = os.listdir(dir)

for folder in folders:
    files = os.listdir(dir + "\\" + folder)
    if len(files) <= 50:
        if len(files) > 40:
            print(folder)