import pytest

from src.phone import Phone


@pytest.fixture
def sample_phone_class():
    return Phone("iPhone 14", 120000, 5, 2)


def test_init(sample_phone_class):
    assert sample_phone_class.name == 'iPhone 14'
    assert sample_phone_class.price == 120000
    assert sample_phone_class.quantity == 5
    assert sample_phone_class.number_of_sim == 2

    sample_phone_class.number_of_sim = 100
    assert sample_phone_class.number_of_sim == 100


def test_str(sample_phone_class):
    assert str(sample_phone_class) == 'iPhone 14'


def test_repr(sample_phone_class):
    assert repr(sample_phone_class) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_errors(sample_phone_class):
    with pytest.raises(ValueError):
        sample_phone_class.number_of_sim = 0
