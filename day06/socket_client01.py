import socket
client = socket.socket()
client.connect(('localhost',1234))
while True:
    cmd = input('>>:')
    if len(cmd) == 0 :
        continue
    client.send(cmd.encode())
    cmd_res_size = client.recv(1024)
    print('命令结果大小',cmd_res_size)
    reversed_size = 0
    reversed_data = b''
    while reversed_size< int(cmd_res_size.decode()):
        data = client.recv(1024)
        print(reversed_size)
        reversed_size+=len(data)
        reversed_data+=data
    else:
        print('cmd res recive done',reversed_size)
        print(reversed_data.decode())
client.close()

