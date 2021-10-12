import pytest


def raise_type_error():
    raise TypeError()


def test_raise_type_error():
    with pytest.raises(TypeError):
        raise_type_error()
