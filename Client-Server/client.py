from socket import socket, AF_INET, SOCK_STREAM
import json
import time
import argparse
import sys


def get_presence_msg():
    presence_msg = json.dumps({"action": "presence",
                               "time": time.ctime(time.time()),
                               "type": "status",
                               "user": {
                                   "account_name": "DragonARRR",
                                   "status": "Yep, I am here!"
                               }})
    return presence_msg


def server_response(code):
    if code is 200:
        print('Подключение прошло успешно.')
        return True
    else:
        print('Проблемы подключения. Код: {}'.format(code))
        return False


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='localhost')
parser.add_argument('-p', '--port', default=7777)

namespace = parser.parse_args(sys.argv[1:])
addr = namespace.addr
port = int(namespace.port)

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((addr, port))   # Соединиться с сервером

presence_msg = get_presence_msg()
s.send(presence_msg.encode('utf-8'))

msg_from_server = s.recv(1024).decode('utf-8')
print("Сообщение от сервера: %s" % msg_from_server)
code = json.loads(msg_from_server).get('response')
server_response(code)

s.close()
