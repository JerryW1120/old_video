import os
dir = "D:\原始2分场景"

folders = os.listdir(dir)

for folder in folders:
    the_list = folder.split(" ")
    if the_list[0] == the_list[-1]:
        print(folder)