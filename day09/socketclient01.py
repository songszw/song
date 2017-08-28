import socket
client = socket.socket()
client.connect(('localhost',8990))
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode())
    data = client.recv(1024)
    print('recv:',data.decode())
client.close()


