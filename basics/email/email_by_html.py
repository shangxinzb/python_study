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
<table>
    <tr>
        <th>函数</th>
        <th>描述</th>
    </tr>
    <tr>
        <td colspan="2">服务器端套接字</td>
    </tr>
    <tr>
        <td>s.bind()</td>
        <td>绑定地址(host,port)到套接字，在AF_INET下，以元组(host,port)的形式表示地址。</td>
    </tr>
    <tr>
        <td>s.listen()</td>
        <td>开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设定为5就可以了。</td>
    </tr>
    <tr>
        <td>s.accept()</td>
        <td>被动接受TCP客户端连接，(阻塞式)等待连接的到来</td>
    </tr>
    <tr>
        <td colspan="2">客户端套接字</td>
    </tr>
    <tr>
        <td>s.content()</td>
        <td>主动初始化TCP服务器连接。一般address的格式为元组(hostname,port)，如果连接出错，返回socket.error错误。</td>
    </tr>
    <tr>
        <td>s.content_ex()</td>
        <td>connect()函数的扩展版本,出错时返回出错码,而不是抛出异常。</td>
    </tr>
    <tr>
        <td colspan="2">公共用途的套接字函数</td>
    </tr>
    <tr>
        <td>s.recv()</td>
        <td>接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。</td>
    </tr>
    <tr>
        <td>s.send()</td>
        <td>发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。</td>
    </tr>
    <tr>
        <td>s.sendall()</td>
        <td>完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。</td>
    </tr>
</table>
<img src="https://www.baidu.com/link?url=iTB2rLOT6j3y-PPum-SfmbitXLZHr8ZIovYv8nFR0tWGVtqRX_hjYEP-PYktYpqb2RbbHD8Woh-E2Ml_kg5kJOMEQFuHktPvig4egNtsypK&wd=&eqid=bfd2e473000d8b5500000005605618d9" alt="一个随便的图片">
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

