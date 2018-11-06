import socket
import threading

data_log = {}  # Словарь вида {name1: [message1, message2, ...], name2: [message1, message2, ...], ...}


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print(address)
            client.settimeout(60)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    def listenToClient(self, client, address=None):
        size = 1024
        while True:
            try:

                client.send(b"Enter your name: ")
                name = client.recv(1024)

                if name not in data_log:
                    data_log[name] = []
                else:
                    pass

                while True:
                    message = client.recv(1024)
                    if not message:
                        break
                    data_log[name].append(message)
                    print(f'This was recieved from client: {message}')
                    client.send(b'Your message was delivered')

            except AssertionError as error:
                print(error)
                return False

            client.close()


if __name__ == "__main__":
    while True:
        port_num = input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('', port_num).listen()
