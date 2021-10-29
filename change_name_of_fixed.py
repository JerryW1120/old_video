import os
from tqdm import tqdm
from time import sleep

path_og = "G:\原始1png"
path_fixed = "E:\修复1png"
file_og = os.listdir(path_og)
file_fixed = os.listdir(path_fixed)

file_og.sort()
file_fixed.sort()

count = 0

    
for file in file_fixed:
    
    os.rename('E:\修复1png\\' + file, 'E:\修复1png\\' + file_og[count])
    print("rename %s successfully to %s" % (file, file_og[count]))
    count += 1

print("finish")