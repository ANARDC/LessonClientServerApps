import socket

letHOST = '127.0.0.1'

sock = socket.socket()

sock.connect((letHOST, 12345))
print(f'Connected to {letHOST}')

data = sock.recv(1024)
print(f'Server: {data}')

name = input(data)
sock.send(name.encode())

message = input("Enter your message to server (1): ")
counter = 1
while message != "quit":
    sock.send(message.encode())
    counter += 1
    message = input(f"Enter your message to server ({counter}): ")

sock.close()
print(f'Connection with {letHOST} was closed')

input('Press enter to exit')
