"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def sample_item_class():
    return Item('Test_name', 10000, 20)


@pytest.fixture
def sample_phone_class():
    return Phone("iPhone 14", 120000, 5, 2)


def test_init_fields(sample_item_class):
    assert isinstance(sample_item_class.name, str)
    assert isinstance(sample_item_class.price, int)
    assert isinstance(sample_item_class.quantity, int)


def test_calculate_total_price(sample_item_class):
    assert sample_item_class.calculate_total_price() == 200000


def test_apply_discount(sample_item_class):
    sample_item_class.pay_rate = 0.85
    sample_item_class.apply_discount()
    assert sample_item_class.price == 8500


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert isinstance(Item.all[0], Item)


def test_string_to_number():
    assert isinstance(Item.string_to_number('5'), int)
    assert Item.string_to_number('500') == 500
    assert Item.string_to_number('10.0') == 10


def test_name_setter(sample_item_class):
    test_item = sample_item_class
    assert test_item.name == 'Test_name'
    with pytest.raises(Exception):
        test_item.name = "Too_long_name"


def test_repr(sample_item_class):
    ob1 = sample_item_class
    assert repr(ob1) == "Item('Test_name', 10000, 20)"


def test_str(sample_item_class):
    ob1 = sample_item_class
    assert str(ob1) == 'Test_name'


def test_add(sample_item_class, sample_phone_class):
    assert sample_item_class + sample_phone_class == 25
    assert sample_item_class + sample_item_class == 40
    assert sample_phone_class + sample_phone_class == 10
    with pytest.raises(ValueError):
        assert sample_item_class + 5 == 25
        assert sample_phone_class + 1 == 6