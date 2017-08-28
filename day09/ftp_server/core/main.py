import socketserver
import json
import os
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote:'.format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)
            except ConnectionResetError as e:
                print('err',e)
                break

    def put(self,*args):
        '''
        接受客户端文件
        '''
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['filesize']
        f = open(filename,'wb')
        self.request.send(b'200 ok')
        received_size = 0
        while received_size<filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size+=len(data)
        else:
            print('file [%s] has uploaded...'%filename)





if __name__ == '__main__':
    HOST,PORT = 'localhost',8990
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()