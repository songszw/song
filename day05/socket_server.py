# 服务器端
'''
conn就是客户端连过来的服务器端为其生成的一个实例
'''
import socket
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听的端口
server.listen() #监听
print('我要开始等电话')
conn,addr = server.accept() #等待监听
print(conn,addr)
print('电话来了')
while True:
    data = conn.recv(1024)
    print('recv',data.decode())
    conn.send(data.upper())
server.close()





