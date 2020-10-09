from DatabaseController.Connection import Connection


def test_singleton_behaviour():
    c1 = Connection()
    c2 = Connection()
    assert id(c1) == id(c2)

