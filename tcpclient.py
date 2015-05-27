import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9997))
print s.recv(1024)
while True:
    w = raw_input('Say:')
    s.send(w)
    print s.recv(1024)
    if w == 'exit':
        break
s.close()
