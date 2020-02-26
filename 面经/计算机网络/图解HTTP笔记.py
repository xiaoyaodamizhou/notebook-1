# TCP/Ip结构分层{
# 应用层：为用户提供服务是通信的活动
# 传输层：处于网络连接中的两台计算机之间的数据传输{
# 三次握手（syn,ack）
# }
# 网络层：处理网络上的流动数据包
# 链路层：链接网络的硬件部分（操作系统，网卡，光纤）
# }

# URI: uniform resourceful indentify{
#   某个协议方案表示的资源的定位标识符）
#   ftp, http, mailto, telnet, file
# }

# URL: uniform resourceful location

# http报文——》用户数据报（报文段）-》包-》帧
# 请求报文:
'''
GET /index.html HTTP/1.1
Host: hacker.jp
Connection: keep-alive（持久连接，减少通讯量的开销）
Content-Type: applicaiton/x-ww-form-urlencoded
Content-Length: 16

name=ueno&age=37
'''
# 响应报文:
'''
HTTP/1.1 200 VERY OK
Date: Tue, 10 Jul 2012 06:50:15 GMT
Content-Length: 355
Content-Type: text/html

<html></html>
'''

# HTTP/1.1 是无状态协议，但是可以用COOKIE保存状态

# 告知服务器意图的HTTP方法:{
# GET 请求访问已经被URI识别的资源
# POST 传输实体主体
# PUT 传输文件
# DELETE 删除文件
# HEAD 获取报文首部
# OPTIONS 查询针对请求URI指定的资源支持方法
# TRACE 追踪路径
# CONNECT 要求用隧道协议链接代理
# LINK 建立与资源之间的联系
# UNLINK 断开连接关系
# }

# 管线化{
# 无需发送请求后等待响应，可以同时发送多个请求
# }

# 关于COOKIE的状态管理{
# 服务器发送响应时候会在响应首部添加Set-Cookie，通知客户端保存Cookie.
# 当下一次客户端再次向服务器发送请求时，自动将请求报文中的COOKIE值发送出去。
# 服务器检查cookie,通过服务器上的记录，最后得到之前的状态信息
# }

# 常见状态码
'''
200	OK	请求成功。一般用于GET与POST请求
201	Created	已创建。成功请求并创建了新的资源
202	Accepted 已接受。已经接受请求，但未处理完成
No Content	无内容。服务器成功处理，
但未返回内容。在未更新网页的情况下，可确保浏览器继续显示当前文档
'''
'''
301	Moved Permanently	永久移动。请求的资源已被永久的移动到新URI，返回信息会包括新的URI，浏览器会自动定向到新URI。今后任何新的请求都应使用新的URI代替
302	Found	临时移动。与301类似。但资源只是临时被移动。客户端应继续使用原有URI
303	See Other	查看其它地址。与301类似。使用GET和POST请求查看
304	Not Modified	未修改。所请求的资源未修改，服务器返回此状态码时，不会返回任何资源。客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源
'''
'''
400	Bad Request	客户端请求的语法错误，服务器无法理解
403	Forbidden	服务器理解请求客户端的请求，但是拒绝执行此请求
404	Not Found	服务器无法根据客户端的请求找到资源（网页）。通过此代码，网站设计人员可设置"您所请求的资源无法找到"的个性页面
'''

'''
500	Internal Server Error	服务器内部错误，无法完成请求
'''

