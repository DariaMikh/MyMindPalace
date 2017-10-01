from socket import socket, AF_INET, SOCK_STREAM
import argparse
import sys
import json


def get_response_msg():
    response_msg = json.dumps({"response": 200,
                               "alert": "OK. Hello!"
                               })
    return response_msg


parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='localhost')
parser.add_argument('-p', '--port', default=7777)

namespace = parser.parse_args(sys.argv[1:])
addr = namespace.addr
port = int(namespace.port)

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
s.bind((addr, port))
s.listen(5)

while True:
    client_socket, client_addr = s.accept()  # Принять запрос на соединение
    print("Получен запрос на соединение от %s" % str(client_addr))

    msg_from_client = client_socket.recv(1024).decode('utf-8')
    print("Сообщение от клиента: %s" % msg_from_client)

    response_msg = get_response_msg()
    client_socket.send(response_msg.encode('utf-8'))

    client_socket.close()
