"""
在html文本中添加图片
"""

import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
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

# msgRoot = MIMEMultipart('related')
msgRoot = MIMEMultipart()

msgRoot['From'] = Header("发件人", 'utf-8')
msgRoot['To'] = Header("收件人", 'utf-8')
msgRoot['Subject'] = Header("标题", 'utf-8')

# 有道翻译：新的多型标头规格
msgAlternative = MIMEMultipart('alternative')
# attach 附加
# alternative 替代
msgRoot.attach(msgAlternative)

mail_msg = """
<img src="cid:img_1" alt="这是一个图片">
"""

msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

# 指定图片为当前目录
# "r" 读取 "b" 二进制
msg_image = MIMEImage(open('images/img.png', 'rb').read())

# 定义图片ID，在HTML文本中引用
msg_image.add_header('Content-ID', 'img_1')
msgRoot.attach(msg_image)


try:
    # 声明邮件实例
    smtpObj = smtplib.SMTP()
    # 连接smtp
    smtpObj.connect(mail_host, 25)
    # 登录用户名
    smtpObj.login(mail_user, mail_password)
    # 发送邮件
    smtpObj.sendmail(sender, receives, msgRoot.as_string())
    print("send email success")
except smtplib.SMTPException as e:
    print(e)
    print("send email error")