import pytest
import json
from server import get_response_msg


def test_get_response_msg():
    assert json.loads(get_response_msg()).get('response') == 200
