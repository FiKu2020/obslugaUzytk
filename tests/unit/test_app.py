import pytest
from flask import Response

from obslugaUzytk.src.app import get_user

def test_get_user_function_can_be_called() -> None:
    dummy_id = 13254
    accual = get_user(id=dummy_id)
    assert isinstance(accual,Response)