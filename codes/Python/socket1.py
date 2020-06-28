import socket
file= open('httpdetails.txt', 'w+')
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)


while True:
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    file.write(data.decode())


mysock.close()
file.close()
