"""
发送HTML格式的邮件
"""


import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_user = '1198684173@qq.com'
mail_password = 'ykuphsxrqcnmghcc'

# 发件人
sender = '1198684173@qq.com'
# 收件人
receives = ['1299303701@qq.com']

mail_msg = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2F2c.zol-img.com.cn%2Fproduct%2F124_500x2000%2F748%2FceZOdKgDAFsq2.jpg&refer=http%3A%2F%2F2c.zol-img.com.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1618967194&t=99b16087c37b030e3382692b91ff8ea5" alt="一个随便的图片">
<p>Python 邮件发送测试...</p>
<p><a href="http://www.baidu.com">这是一个链接</a></p>
</body>
</html>
"""

message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header('发件人', 'utf-8')
message['To'] = Header('收件人', 'utf-8')

subject = "邮件标题"
message['Subject'] = Header(subject, 'utf-8')

try:
    # 声明邮件实例
    smtpObj = smtplib.SMTP()
    # 连接smtp
    smtpObj.connect(mail_host, 25)
    # 登录用户名
    smtpObj.login(mail_user, mail_password)
    # 发送邮件
    smtpObj.sendmail(sender, receives, message.as_string())
    print("send email success")
except smtplib.SMTPException as e:
    print(e)
    print("send email error")

