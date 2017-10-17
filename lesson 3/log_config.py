import logging
import logging.handlers

# Создаем логгеры все в одном месте, потом будем их получить по имени
# Клиентский логгер
client_logger = logging.getLogger('client')
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s")
client_handler = logging.FileHandler("client.log", encoding='utf-8')
client_handler.setLevel(logging.INFO)
client_handler.setFormatter(formatter)
client_logger.addHandler(client_handler)
client_logger.setLevel(logging.INFO)

# Серверный логгер
server_logger = logging.getLogger('server')
server_handler = logging.handlers.TimedRotatingFileHandler('server.log', when='d')
server_handler.setFormatter(formatter)
server_logger.addHandler(server_handler)
server_logger.setLevel(logging.INFO)
