import socket,os
server = socket.socket()
server.bind(('localhost',1234))
server.listen()
while True:
    conn,addr = server.accept()
    print('new conn',addr)
    while True:
        print('ready to commed')
        data = conn.recv(1024)
        if not data:
            print('connected failed')
            break
        print('execute the commed:',data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res)==0:
            cmd_res = 'cmd has no output'
        conn.send(str(len(cmd_res.encode())).encode())
        client_ack = conn.recv(1024)
        print(client_ack.decode())
        conn.send(cmd_res.encode())
        print('send done')

server.close()



