"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def sample_instance():
    return Item('Test_name', 10000, 20)


def test_init_fields(sample_instance):
    assert isinstance(sample_instance.name, str)
    assert isinstance(sample_instance.price, int)
    assert isinstance(sample_instance.quantity, int)


def test_calculate_total_price(sample_instance):
    assert sample_instance.calculate_total_price() == 200000


def test_apply_discount(sample_instance):
    sample_instance.pay_rate = 0.85
    sample_instance.apply_discount()
    assert sample_instance.price == 8500


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


def test_string_to_number():
    assert isinstance(Item.string_to_number('5'), int)
    assert Item.string_to_number('500') == 500
    assert Item.string_to_number('10.0') == 10


def test_repr(sample_instance):
    ob1 = sample_instance
    assert repr(ob1) == "Item('Test_name', 10000, 20)"


def test_str(sample_instance):
    ob1 = sample_instance
    assert str(ob1) == 'Test_name'