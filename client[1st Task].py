from collections import OrderedDict
import threading
import socket

HOST = '127.0.0.1'


log_data = {}


def hosts_parsing(start_host, end_host):
    number = 1
    for i in range(start_host, end_host):
        progress = (number/(end_host-start_host+1))*100  # Подсчет текущего прогресса в процентах
        number += 1
        char1, char2 = ">", "_"
        print(f"Completed {int(progress)}% {char1*(int(progress)//5)}{char2*(20-int(progress)//5-1)}", end="\r")
        sock = socket.socket()
        try:
            sock.connect((HOST, i))
            log_data[i] = "\033[92mAVAILABLE\033[0m"
        except:
            log_data[i] = "\033[91mUNAVAILABLE\033[0m"
        sock.close()


# Тут сначала первый поток работает, потом как первый заканчивает запускается второй
t = threading.Thread(target=hosts_parsing, args=(1, 501))
t.start()
while t.is_alive() is True:
    pass
if t.is_alive() is False:
    print("\n")
    t = threading.Thread(target=hosts_parsing, args=(501, 1001))
    t.start()
while t.is_alive() is True:
    pass
print("\n")

# Вывод словаря в отсортированном по ключам виде
for i, j in dict(OrderedDict(sorted(log_data.items(), key=lambda k: k[0]))).items():
    print(f"HOST WITH NUMBER {i} IS {j}")
