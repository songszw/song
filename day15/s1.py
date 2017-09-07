import socket
def handle_request(client):
    buf = client.recv(1024)
    client.send(b'HTTP/1.1 200 OK\r\n\r\n')
    client.send(b'Hello,workd')
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8000))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()
        handle_request(conn)
        conn.close()
if __name__ == '__main__':
    main()