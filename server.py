import socket
s = socket.socket()
print("Socket has been created.")

s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connections")

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", address)
    c.send(bytes('You have joined the Mercelis server', 'utf-8'))

    c.close()
