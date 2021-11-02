import os
from posixpath import split
import shutil
import smtplib
from email.mime.text import MIMEText

import matplotlib.pyplot as plt
import numpy as np
from skimage.metrics import peak_signal_noise_ratio

dir_origin = "D:\原始2分场景"
folders = os.listdir(dir_origin)
folders.sort()

unusual = []

def send_email(text, subject):
    msg = MIMEText(text + '\n\n这是系统自动发出邮件，请不要回复。', 'plain', 'utf-8')
    msg['From'] = '940341746@qq.com'
    msg['To'] = '940341746@qq.com'
    msg['Subject'] = subject
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


for folder in folders:
    files = os.listdir(dir_origin + '\\' + folder)
    files.sort()
    count = 0
    if len(files) == 1:
        continue
    else:

        while count < len(files) - 1:
            cmpr1 = plt.imread(os.path.join(dir_origin, folder, files[count]))
            cmpr2 = plt.imread(os.path.join(dir_origin, folder, files[count + 1]))
            cmpr1 = np.array(cmpr1)
            cmpr2 = np.array(cmpr2)
            psnr = peak_signal_noise_ratio(cmpr1, cmpr2)##用cv的库要读图片(done)
            print("%s 和 %s 两张图片的psnr是：%d" % (files[count], files[count + 1], psnr))

            if psnr < 19:
                unusual.append(files[count])
            count += 1
        
    text = "文件夹" + folder + "的照片已核对过"
    subject = "文件夹处理"
    send_email(text, subject)


for file in unusual:
    print("%s 文件可能有问题，去查看" % file)

text = "对比结束"
subject = "对比结束"
send_email(text, subject)

