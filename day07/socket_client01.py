import socket
client = socket.socket()
client.connect(('localhost',8990))
while True:
    cmd_msg = input('>>:')
    if len(cmd_msg) == 0: continue
    client.send(cmd_msg.encode())
    msg_size =client.recv(1024)
    print(int(msg_size.decode()))
    data_size = 0
    data_val = b''
    print(int(msg_size.decode()))
    client.send(msg_size)
    while data_size<int(msg_size.decode()):
        data = client.recv(1024)
        data_size+=len(data)
        data_val+=data
        print('共收取资料:',data_size)
    else:
        print(data_val.decode())


client.close()