import pytest

from obslugaUzytk.src.controlers import GetUserControler


def test_controler_can_be_instantiated() -> None:
    Controler = GetUserControler()
    assert  isinstance(Controler,GetUserControler)

def test_raises_on_user_method()-> None:
    controler = GetUserControler()
    with pytest.raises(NotImplementedError):
        controler.get_user()