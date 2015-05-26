import socket
port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    word = raw_input("Please input:")
    s.sendto(word,(host,port))
