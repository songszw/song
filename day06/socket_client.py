import socket,os
client = socket.socket()
client.connect(('localhost',8990))
while True:
    msg = input('>>:').strip()
    if len(msg) == 0 : continue
    client.send(msg.encode('utf-8'))
    msg_res_size = client.recv(1024) #接受命令结果的长度
    print('命令结果大小',msg_res_size.decode())
    received_data = b''
    received_size = 0
    while received_size < int(msg_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        print(received_size)
        # print(data.decode())
        received_data+=data
    else:
        print('msg receive Done')
        print(received_data.decode())


client.close()
