import socket,os
server = socket.socket()
server.bind(('localhost',1234))
server.listen()
while True:
    conn,addr = server.accept()
    print('new conn',addr)
    while True:
        print('正在等待新指令')
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        print('新指令:',data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output'

        conn.send(str(len(cmd_res.encode())).encode())
        conn.send(cmd_res.encode())
        print('send done')

server.close()