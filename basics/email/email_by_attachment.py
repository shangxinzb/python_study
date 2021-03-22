"""
发送带附件的邮件
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_user = '1198684173@qq.com'
mail_password = 'ykuphsxrqcnmghcc'

# 发件人
sender = '1198684173@qq.com'
# 收件人
receives = ['1299303701@qq.com']

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("发件人", 'utf-8')
message['To'] = Header("收件人", 'utf-8')
message['Subject'] = Header("标题", 'utf-8')

# 邮件正文内容
message.attach(MIMEText("发送邮件测试", 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的test.txt文件
att1 = MIMEText(open('docs/test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1['Content-Disposition'] = 'attachment; filename="test1.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的test2.txt文件
att2 = MIMEText(open('docs/test2.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att2['Content-Disposition'] = 'attachment; filename="test2.txt"'
message.attach(att2)

# 发送邮件
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_password)
    smtpObj.sendmail(sender, receives, message.as_string())
    print("发送邮件成功。")
except smtplib.SMTPException as e:
    print(e)
    print("发送邮件失败。")