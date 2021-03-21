# socket 学习

Python 提供了两个级别的访问网络服务：

- 低级别的网络服务支持基本的Socket,它提供了标准的BSD Sockets API，可以访问底层操作系统Socket接口的全部方法
- 高级别的网络服务模块 SocketServer，它提供了服务器中心类，可简化网络服务器的开发
---
## 什么是Socket
Socket又称“套接字”，应用程序通常通过“套接字”向网络发出请求或者应答网络请求，
使主机间或者一台计算机上的进程间可以通讯。
---
## Socket()函数
Python中，我们用socket()函数来创建套接字，语法格式如下：
```python
socket.socket([family[, type[, proto]]])
```
### 参数

- family:套接字家族可以使AF_UNIX或者AF_INET
- type:套接字类型可以根据是面向连接还是非连接分为SOCK_STREAM或SOCK_DGRAM
- protocol:一般不填默认为0


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
</table>