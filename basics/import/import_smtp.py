"""
引入邮箱功能
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方SMTP服务
mail_host = 'smtp.qq.com'
mail_user = '1198684173@qq.com'
mail_password = 'password'

# 发件人
sender = '1198684173@qq.com'
# 收件人
receives = ['1299303701@qq.com']
# 邮件消息内容 plian是默认的
message = MIMEText('python的第一封邮件', 'plain', 'utf-8')
# 发件人名称
message["From"] = Header('1198684173@qq.com', 'utf-8')
# 收件人名称
message['To'] = Header('who receive', 'utf-8')
message['Subject'] = Header('这是邮件的标题吗？', 'utf-8')

try:
    # 初始化smtp
    smtpObj = smtplib.SMTP()
    # 链接qq的smtp hsot地址
    smtpObj.connect(mail_host, 25)  # 25为SMTP端口号
    # 登录
    smtpObj.login(mail_user, mail_password)
    # 发送邮件
    smtpObj.sendmail(sender, receives, message.as_string())
    print("邮件发送成功。")
except smtplib.SMTPException as e:
    print(e)
    print("邮件发送失败。")
