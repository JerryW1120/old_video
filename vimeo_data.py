import os
from posixpath import split
import shutil
import smtplib
from email.mime.text import MIMEText

import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import peak_signal_noise_ratio

input_dir_origin = "G:\原始2png"
output_dir_orngin = "D:\原始2分场景"
input_dir_fixed = "G:\修复2png"
output_dir_fixed = "D:\修复2分场景"
all_file = os.listdir(input_dir_origin)
all_file.sort()


def split_fold(baseline, count, png_list):
    png_list.append(all_file[baseline])
    while 1:        
        if count >= len(all_file):#文件尾问题解决
            if len(png_list) == 1:
                print("已到达文件结尾，分类结束")
                msg = MIMEText('原始2和修复2搞定了\n\n这是系统自动发出邮件，请不要回复。', 'plain', 'utf-8')
                msg['From'] = '940341746@qq.com'
                msg['To'] = '940341746@qq.com'
                msg['Subject'] = '原始2和修复2搞定了'
                from_addr = '940341746@qq.com'
                # 密码是授权码
                password = 'szowquehfogxbgaa'
                to_addr = '940341746@qq.com'
                smtp_server = 'smtp.qq.com'
                # QQ邮箱的SMTP服务需SSL加密，端口为465
                server = smtplib.SMTP_SSL(smtp_server)
                # 显示发送过程
                server.set_debuglevel(1)
                # 登陆验证
                server.login(from_addr, password)
                # 发送邮件
                server.sendmail(from_addr, [to_addr], msg.as_string())
                # 退出
                server.quit()
                exit()
            else:
                return count, baseline, png_list
        else:           
            cmpr1 = plt.imread(os.path.join(input_dir_origin, all_file[count - 1]))
            cmpr2 = plt.imread(os.path.join(input_dir_origin, all_file[count]))
            cmpr1 = np.array(cmpr1)
            cmpr2 = np.array(cmpr2)
            psnr = peak_signal_noise_ratio(cmpr1, cmpr2)##用cv的库要读图片(done)
            print("%s 和 %s 两张图片的psnr是：%d" % (all_file[count - 1], all_file[count], psnr))
            if psnr >= 16: #解决两帧之间是不同分镜的问题
                png_list.append(all_file[count])
                print("将图片%s放入列表中" % (all_file[count]))
                # print(count_of_png)
                count += 1
            else:
                #分镜不一样了就更新baseline
                baseline = count
                count += 1
                print("判断为两个分镜的图片，去创建文件夹")
                return count, baseline, png_list
                
            
#返回pnglist两个目的：1.复制文件；2.列表首尾就是文件夹名字
    

def copyfile(sourcefile, destanationfile):
    if not os.path.isfile(sourcefile):
        print ("%s not exist!" % (sourcefile))
    else:
        shutil.copy(sourcefile, destanationfile)          # 复制文件
        print ("copy %s -> %s" % (sourcefile, destanationfile))

count = 1
baseline = 0

while count <= len(all_file):
    png_list = []
    answer = split_fold(baseline, count, png_list)
    count = answer[0]
    baseline = answer[1]
    img_list = answer[2]


    folder_dir_origin = os.path.join(output_dir_orngin, str(img_list[0].split(".")[0]) + ' - ' + str(img_list[-1].split(".")[0]))
    os.makedirs(folder_dir_origin)
    print("已创建文件夹%s" % (folder_dir_origin))

    folder_dir_fixed = os.path.join(output_dir_fixed, str(img_list[0].split(".")[0]) + ' - ' + str(img_list[-1].split(".")[0]))
    os.makedirs(folder_dir_fixed)
    print("已创建文件夹%s" % (folder_dir_fixed))
            
    for file in answer[2]:
        copyfile(input_dir_origin + '\\' + str(file), folder_dir_origin + '\\' + str(file))
        copyfile(input_dir_fixed + '\\' + str(file), folder_dir_fixed + '\\' + str(file))
    
