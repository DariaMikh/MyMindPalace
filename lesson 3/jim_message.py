import time
from errors import ResponseCodeLenError, ResponseCodeError, UsernameToLongError, MandatoryKeyError


class JIMMessage:
    @staticmethod
    def get_authenticate_msg(account_name, password):
        if not isinstance(account_name, str):
            raise TypeError
        if len(account_name) > 25:
            raise UsernameToLongError(account_name)

        return {
            "action": "authenticate",
            "time": time.time(),
            "user": {
                "account_name": account_name,
                "password": password
            }
        }

    @staticmethod
    def get_response_to_authentication(code, message=''):
        if len(code) != 3:
            raise ResponseCodeLenError(code)
        if code[0] not in '1245':
            raise ResponseCodeError(code)

        if code == 200:
            return {
                "response": code,
                "alert": message
            }
        if code == 402:
            return {
                "response": code,
                "error": "Wrong password or no account with that name"
            }
        if code == 409:
            return {
                "response": code,
                "error": "Someone is already connected with the given user name"
            }

    @staticmethod
    def quite_msg():
        return {
            "action": "quit"
        }

    @staticmethod
    def get_presence_msg(account_name="Guest", presence_type='', type_msg=''):
        msg = {}
        if len(account_name) > 25:
            raise UsernameToLongError(account_name)
        if not isinstance(account_name, str):
            raise TypeError
        if presence_type and not type_msg:
            raise MandatoryKeyError

        msg["action"] = "presence"
        msg["time"] = time.time()
        if presence_type:
            msg["presence_type"] = presence_type
        msg["user"] = {}
        msg["user"]["account_name"] = account_name
        if presence_type:
            msg[str(presence_type)] = type_msg

        return msg

    @staticmethod
    def get_probe_request():
        return {
            "action": "probe",
            "time": time.time()
        }

    @staticmethod
    def get_msg(msg):
        return {
            "action": "msg",
            "time": time.time(),
            "message": str(msg)
        }
