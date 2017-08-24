import socket,os
server = socket.socket()
server.bind(('localhost',8990))
server.listen()
while True:
    conn,addr = server.accept()
    print('new conn',addr)

    while True:
        print('ready to commed')
        msg = conn.recv(1024)
        if not msg:
            msg = 'cmd has no output'
            break
        print('收到指令：',msg)
        data = os.popen(msg.decode()).read()
        conn.send(str(len(data.encode())).encode())
        client_a = conn.recv(1024)
        conn.send(data.encode())

server.close()