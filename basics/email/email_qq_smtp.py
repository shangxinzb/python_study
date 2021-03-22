"""
使用QQ smtp
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_port = 25
mail_user = '1198684173@qq.com'
mail_password = 'ykuphsxrqcnmghcc'
mail_sender = '1198684173@qq.com'
mail_receive = '1299303701@qq.com'

try:
    message = MIMEText("发送邮件的内容", 'plain', 'utf-8')
    message['From'] = formataddr(['哲别', mail_sender])
    message['To'] = formataddr(['傀儡', mail_receive])
    message['Subject'] = "这个标题竟然不需要用Header"

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_password)
    smtpObj.sendmail(mail_sender, [mail_receive, ], message.as_string())
    print('success')
except smtplib.SMTPException as e:
    print(e)
    print("error")
