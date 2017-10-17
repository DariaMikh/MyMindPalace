import time
import json
from pytest import raises
from errors import UsernameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from jim_message import JIMMessage


def test_get_presence_msg():
    # без параметров
    message = JIMMessage.get_presence_msg()
    assert message['action'] == "presence"
    # берем разницу во времени
    assert abs(message['time'] - time.time()) < 0.1
    assert message["user"]["account_name"] == 'Guest'

    # с именем
    message = JIMMessage.get_presence_msg('test_user_name')
    assert message["user"]["account_name"] == 'test_user_name'

    # неверный тип
    with raises(TypeError):
        JIMMessage.get_presence_msg(200)
    with raises(TypeError):
        JIMMessage.get_presence_msg(None)

    # Имя пользователя слишком длинное
    with raises(UsernameToLongError):
        JIMMessage.get_presence_msg('11111111111111111111111111')


def test_get_authenticate_msg():
    # с именем
    message = JIMMessage.get_authenticate_msg('test_user_name', 'test_password')
    assert message["user"]["account_name"] == 'test_user_name'
    assert message["user"]["account_name"] == 'test_password'

    # неверный тип
    with raises(TypeError):
        test_get_presence_msg(200)
    with raises(TypeError):
        test_get_presence_msg(None)

    # Имя пользователя слишком длинное
    with raises(UsernameToLongError):
        test_get_presence_msg('11111111111111111111111111')


def test_get_response_to_authentication():
    with raises(ResponseCodeLenError):
        message = JIMMessage.get_response_to_authentication(1234)
    with raises(ResponseCodeError):
        message = JIMMessage.get_response_to_authentication(866)

    message = JIMMessage.get_response_to_authentication(200)
    assert message["response"] == 200
    message = JIMMessage.get_response_to_authentication(409)
    assert message["error"] == "Wrong password or no account with that name"
    message = JIMMessage.get_response_to_authentication(409)
    assert message["error"] == "Someone is already connected with the given user name"


def test_get_probe_request():
    message = JIMMessage.get_probe_request()
    assert message["action"] == "probe"
