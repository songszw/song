# 客户端
import socket
# 声明协议类型，同时生成socket链接对象
client = socket.socket()
client.connect(('localhost',6969))
while True:
    msg = input('>>:').strip()
    if len(msg)==0:
        print('内容不可以为空')
    else:
        client.send(msg.encode(encoding='utf-8'))
        data = client.recv(1024)
        print('recv:',data.decode())
client.close()


