from socket import socket, AF_INET, SOCK_STREAM
from errors import WrongModeError
import json
from jim_message import JIMMessage
import argparse
import sys

import logging
import log_config
from decorators import Log

# Получаем по имени клиентский логгер, он уже нестроен в log_config
logger = logging.getLogger('client')
# создаем класс декоратор для логирования функций
log = Log(logger)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default='localhost')
parser.add_argument('-p', '--port', default=7777)
parser.add_argument('-m', '--mode', default='r')


class Client:
    @log
    def __init__(self, addr='localhost', port=7777, mode='r'):
        """
            Создание клиентского подключения
            :param addr: адрес
            :param port: порт
            :param mode: чтение или запись
        """
        # Создать сокет TCP
        self.s = socket(AF_INET, SOCK_STREAM)
        # Соединиться с сервером
        self.s.connect((addr, port))
        self.mode = mode

    def main_loop(self):
        """
            Цикл приема и отправки сообщений в зависимости от режима
        """
        if self.mode == 'r':
            # читаем сообщения и выводим на экран
            while True:
                # Принять не более 1024 байтов данных
                jmessage = self.s.recv(1024).decode('utf-8')
                # Словарь переводим в json
                message = json.dumps(jmessage)
                # Просто выводим сообщение пришедшее от других пользователей
                if message["action"] == "msg":
                    print(message["action"])
        elif self.mode == 'w':
            # ждем ввода сообщения и шлем на сервер
            while True:
                message_str = input(':>')
                message = json.dumps(JIMMessage.get_msg(message_str))
                # Отсылаем сообщение в байтах
                self.s.send(message.encode(encoding='utf-8'))
        else:
            raise WrongModeError(self.mode)


if __name__ == '__main__':
    # Получаем параметры скрипта
    namespace = parser.parse_args(sys.argv[1:])
    addr = namespace.addr
    try:
        port = int(namespace.port)
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    mode = namespace.mode
    if mode not in ('r', 'w'):
        print('Режим должен быть r - чтение, w - запись')
        sys.exit(0)

    # Создаем подключение
    s = Client(addr, port, mode)
    # Запускаем главный цикл
    s.main_loop()
