import pytest

from src.keyboard import Keyboard


@pytest.fixture
def sample_keyboard_class():
    return Keyboard('Super Keyboard', 2000, 10)


def test_init(sample_keyboard_class):
    assert sample_keyboard_class.name == 'Super Keyboard'
    assert sample_keyboard_class.price == 2000
    assert sample_keyboard_class.quantity == 10
    assert sample_keyboard_class.language == 'EN'


def test_change_lang(sample_keyboard_class):
    assert sample_keyboard_class.language == 'EN'
    sample_keyboard_class.change_lang()
    assert sample_keyboard_class.language == 'RU'
    sample_keyboard_class.change_lang()
    assert sample_keyboard_class.language == 'EN'
