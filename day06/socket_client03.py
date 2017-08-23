'''
    close
        优衣库
        H&M
        ZARA
    shoes
        tiger
'''
import socket
client = socket.socket()
client.connect(('localhost',1234))
while True:
    cmd = input('>>:')
    if len(cmd)==0:
        continue
    client.send(cmd.encode())
    msg = client.recv(1024)
    print('commed size is :',msg)
    client.send('ready to send'.encode('utf-8'))
    receive_size = 0
    receive_data = b''
    while int(msg.decode()) >receive_size:
        data = client.recv(1024)
        receive_size+=len(data)
        receive_data+=data
    else:
        print('commed dowm',receive_size)
        print(receive_data.decode())
client.close()
