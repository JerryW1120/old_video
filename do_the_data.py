import os
import shutil
import yagmail

import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import peak_signal_noise_ratio

input_dir = "G:\原始1png"
output_dir = "D:\\"
all_file = os.listdir(input_dir)
all_file.sort()


def whether_7(baseline, count_of_vimeo, png_7list):
    count_of_png = 0
    end = 0
    png_7list.append(all_file[baseline])
    while count_of_png < 6:
        if count_of_vimeo == len(all_file):#文件尾问题解决
            print("已到达文件结尾，分类结束")
            yag = yagmail.SMTP(user = '940341746@qq.com', password = 'szowquehfogxbgaa', host = 'smtp.qq.com')
# 发送邮件
            yag.send(to = ['940341746@qq.com'], subject = '原始1png完事了', contents = ['原始1png完事了，火速搞原始2的'])
            exit()
        else:           
            cmpr1 = plt.imread(os.path.join(input_dir, all_file[count_of_vimeo - 1]))
            cmpr2 = plt.imread(os.path.join(input_dir, all_file[count_of_vimeo]))
            cmpr1 = np.array(cmpr1)
            cmpr2 = np.array(cmpr2)
            psnr = peak_signal_noise_ratio(cmpr1, cmpr2)##用cv的库要读图片(done)
            print("%s 和 %s 两张图片的psnr是：%d" % (all_file[count_of_vimeo - 1], all_file[count_of_vimeo], psnr))
            if psnr >= 16: #解决两帧之间是不同分镜的问题
                png_7list.append(all_file[count_of_vimeo])
                print("将图片%s放入列表中" % (all_file[count_of_vimeo]))
                # print(count_of_png)
                count_of_vimeo += 1
                count_of_png += 1
            else:
                baseline = count_of_vimeo
                print("判断为两个分镜的图片，跳出循环")
                break

    return count_of_vimeo, baseline, png_7list, end

def copyfile(sourcefile, destanationfile):
    if not os.path.isfile(sourcefile):
        print ("%s not exist!"%(sourcefile))
    else:
        shutil.copy(sourcefile, destanationfile)          # 复制文件
        print ("copy %s -> %s" % (sourcefile, destanationfile))

# 要分两层子文件夹

count_outside = 1
count_of_vimeo = 0
baseline = 0

while count_of_vimeo <= len(all_file):
    father_folder_dir = os.path.join(output_dir, str(count_outside).zfill(5))
    os.makedirs(father_folder_dir)
    print("已创建一级文件夹%s" % (father_folder_dir))
    count_inside = 1
    while count_inside <= 1000:
        count_of_vimeo = baseline + 1
        png_7list = []
        answer = whether_7(baseline, count_of_vimeo, png_7list)
        
        if answer[0] - answer[1] != 7:
            baseline = answer[1]
            continue
        else:
            son_folder_dir = os.path.join(output_dir, father_folder_dir, str(count_inside).zfill(4))
            os.makedirs(son_folder_dir)
            print("已创建二级文件夹%s" % (son_folder_dir))
            count = 1
            for file in answer[2]:
                copyfile(input_dir + '\\' + str(file), son_folder_dir + '\\' + 'img' + str(count) + '.png')
                count += 1
            count_inside += 1
            baseline += 3

    
    count_outside += 1