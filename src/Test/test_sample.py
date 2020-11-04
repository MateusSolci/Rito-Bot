from Database_Controller.connection import Connection
from API_Requests.any_request import make_request

def test_singleton_behaviour():
    c1 = Connection()
    c2 = Connection()
    assert id(c1) == id(c2)


def test_generic_request():
    response = make_request("url")
    assert response == "*Bad Request*"