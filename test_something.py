import os

input_dir = "/Users/jerryw/Desktop/文档/老电影修复/dpx文件"
all_file = os.listdir(input_dir)
all_file.sort()

print(all_file)