import select
import sys
from socket import socket, AF_INET, SOCK_STREAM
import json
from jim_message import JIMMessage
import argparse

import logging
import log_config
from decorators import Log

# Получаем серверный логгер по имени, он уже объявлен в log_config и настроен
logger = logging.getLogger('server')
log = Log(logger)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='localhost')
parser.add_argument('-p', '--port', default=7777)


class Server:
    @log
    def __init__(self, addr, port):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.bind((addr, port))
        self.s.listen(10)
        self.s.settimeout(0.2)
        self.all_clients = []
        self.r_clients = []  # Клиенты, которые могут отправлять сообщения.
        self.w_clients = []  # Клиенты, которые читают сообщения.
        self.messages = []

    @log
    def read_messages(self):
        """
            Чтение сообщений, которые будут посылать клиенты.
        """

        # Очистка списка входящих сообщений.
        self.messages = []

        for sock in self.r_clients:
            try:
                jmsg = sock.recv(1024).decode('utf-8')
                # преобразуем json в словарь
                msg = json.loads(jmsg)
                if msg["action"] == "msg":
                    self.messages.append(msg)
                else:
                    pass    # Пока ничего не делаем.
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                self.all_clients.remove(sock)

    @log
    def write_messages(self):
        ''' Ответ сервера клиентам
        '''
        # Каждому пользователю чата (клиент на запись)
        # отправим все присылаемые сообщения (от клиентов на чтение).
        for sock in self.w_clients:
            try:
                for msg in self.messages:
                    # Подготовить и отправить ответ сервера
                    sock.send(json.dumps(JIMMessage.get_msg(msg)).encode('utf-8'))
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                self.all_clients.remove(sock)

    def main_loop(self):
        while True:
            try:
                conn, addr = self.s.accept()  # Проверка подключений
            except OSError as e:
                pass  # timeout вышел
            else:
                print("Получен запрос на соединение от %s" % str(addr))
                # Добавляем клиента в список
                self.all_clients.append(conn)
            finally:
                # Проверить наличие событий ввода-вывода
                wait = 0
                self.r_clients = []
                self.w_clients = []
                try:
                    self.r_clients, self.w_clients, e = select.select(self.all_clients, self.all_clients, [], wait)
                except:
                    pass  # Ничего не делать, если какой-то клиент отключился

                self.read_messages()  # Получаем входные сообщения
                self.write_messages()  # Выполним отправку входящих сообщений


if __name__ == '__main__':
    print('Запуск сервера')
    # Получаем аргументы скрипта
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    try:
        port = int(namespace.port)
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)

    server = Server(addr, port)
    server.main_loop()
