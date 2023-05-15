"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture


def sample_instance():
    return Item('name', 10000, 20)


def test_init_fields(sample_instance):
    assert sample_instance.name == 'name'
    assert sample_instance.price == 10000
    assert sample_instance.quantity == 20


def test_calculate_total_price(sample_instance):
    assert sample_instance.calculate_total_price() == 200000


def test_apply_discount(sample_instance):
    sample_instance.pay_rate = 0.85
    sample_instance.apply_discount()
    assert sample_instance.price == 8500