import socket,hashlib
client = socket.socket()
client.connect(('localhost',1991))
while True:
    cmd = input('>>:')
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        file_size = int(client.recv(1024).decode())
        print('server file size : ',file_size)
        client.send(b'ready to recievd')
        recive_size = 0
        filename = cmd.split()[1].split('.')[0]
        fileend = cmd.split()[1].split('.')[1]
        f = open((filename+'new.'+fileend),'wb')
        file_md5 = hashlib.md5()
        while recive_size < file_size:
            if file_size<1024:
                size = file_size
            elif file_size-recive_size<=1024:
                size = 1024
            else:
                size = file_size-recive_size
            data = client.recv(size)
            recive_size += size
            file_md5.update(data)
            f.write(data)
        else:
            f.close()
            client_md5 = file_md5.hexdigest()
            server_md5 = client.recv(1024)
            print('client_file_size',recive_size)
            print('client_md5:',client_md5,'server_md5',server_md5)
client.close()