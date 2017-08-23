import socket
client = socket.socket()
client.connect(('localhost',1024))
while True:
    cmd = input('>>:')
    if len(cmd)==0:
        continue
    client.send(cmd.encode())
    cmd_res_size = client.recv(1024)
    print('执行命令大小',cmd_res_size)
    received_data = b''
    received_size = 0
    print(cmd_res_size)
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_data+=data
        received_size+=len(data)
    else:
        print('received done',received_size)
        print(received_data.decode())

client.close()