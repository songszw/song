import socket,os,hashlib
server = socket.socket()
server.bind(('localhost',1991))
server.listen()
while True:
    conn,addr = server.accept()
    print('new conn',addr)
    while True:
        data = conn.recv(1024)
        if not data:
            data = 'server out put nothing'
            break
        cmd,filename = data.decode().split()
        if os.path.isfile(filename):
            f = open(filename,'rb')
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            m = hashlib.md5()
            for line in f:
                m.update(line)
                conn.send(line)
            f.close()
            conn.send(m.hexdigest().encode())
server.clode()
 