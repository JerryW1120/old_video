import smtplib
from email.mime.text import MIMEText
# 构造邮件
msg = MIMEText('您的程序已执行完毕，请及时上线检查！\n\n这是系统自动发出邮件，请不要回复。', 'plain', 'utf-8')
msg['From'] = '940341746@qq.com'
msg['To'] = '940341746@qq.com'
msg['Subject'] = '您的程序已执行完毕！'
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