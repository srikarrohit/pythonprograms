import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket object
s.connect(('localhost',8081))
s.send('Happy Coding')
data = s.recv(1024)
s.close()
print 'Receied:'
print data
