import os
import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import peak_signal_noise_ratio



def find_you(dir, base):
    files = os.listdir(dir)
    files.sort()
    list_of_photos = []
   
    for file in files:
        compare = plt.imread(os.path.join(dirs[count], file))
        compare = np.array(compare)
        psnr = peak_signal_noise_ratio(base, compare)
        if psnr >= 15:
            print("文件 %s 和base的psnr值较高，建议查看" % (os.path.join(dirs[count], file)))
            print("psnr为：%d" % psnr)
            list_of_photos.append(file)
        return list_of_photos

dirs = ["G:\修复1png", "G:\修复2png", "G:\原始1png", "G:\原始2png"]
base_dir = "G:\\"
base = plt.imread(os.path.join(base_dir, "L0.png"))
base = np.array(base)

count = 0
while count <= 3:
    similar_photos = find_you(dirs[count], base)
    if len(similar_photos) != 0:
        print(similar_photos)
    else:
        print("文件夹 %d 没有相似图片" % (count + 1))

    count += 1

print("finish")

