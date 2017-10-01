import pytest
import json
from client import get_presence_msg, server_response


def test_get_presence_msg():
    assert json.loads(get_presence_msg()).get('action') == 'presence'


@pytest.mark.parametrize('code', [200, 404, 500])
def test_server_response(code):
    if code is 200:
        assert server_response(code) is True
    else:
        assert server_response(code) is False
