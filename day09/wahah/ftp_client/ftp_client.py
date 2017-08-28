import socket
import os
import json


class FTPClient(object):
    def __init__(self):
        self.client = socket.socket()
    def help(self):
        msg = '''
        dir
        pwd
        cd 
        get filename
        put filename
        
        '''
        print(msg)

    def connect(self,ip,host):
        self.client.connect((ip,host))

    def interactive(self):
        while True:
            cmd = input('>>:').strip()
            if len(cmd)==0:continue
            cmd_str = cmd.split()[0]
            if hasattr(self,'cmd_%s'%cmd_str):
                func = getattr(self,'cmd_%s'%cmd_str)
                func(cmd)
            else:
                self.help()


    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) >1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_dic = {
                    'action':'put',
                    'filename':filename,
                    'filesize':filesize,
                    'overridden':True
                }

                self.client.send(json.dumps(msg_dic).encode())
                #防止粘包，等待服务器确认
                server_response = self.client.recv(1024)
                # if server_response == 200:
                f = open(filename,'rb')
                for line in f:
                    self.client.send(line)
                else:
                    print('send done')
                    f.close()
            else:
                print(filename,' is not exit')
    def cmd_get(self):
        pass

ftp = FTPClient()
ftp.connect('localhost',8990)
ftp.interactive()

