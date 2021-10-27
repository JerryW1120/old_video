import os

input_dir = "/Users/jerryw/Desktop/文档/老电影修复/dpx文件"
all_file = os.listdir(input_dir)

for file in all_file:
    print(str(file))