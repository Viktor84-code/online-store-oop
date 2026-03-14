"""Тесты для абстрактного базового класса BaseCollection."""

import pytest  # ← добавить!

from src.base_collection import BaseCollection
from src.category import Category
from src.order import Order


def test_base_collection_abstract():
    """Проверка, что нельзя создать экземпляр BaseCollection."""
    with pytest.raises(TypeError):
        BaseCollection("Тест", "Описание")


def test_category_inherits_base():
    """Проверка, что Category является наследником BaseCollection."""
    assert issubclass(Category, BaseCollection)


def test_order_inherits_base():
    """Проверка, что Order является наследником BaseCollection."""
    assert issubclass(Order, BaseCollection)


def test_base_collection_has_abstract_methods():
    """Проверка наличия абстрактных методов."""
    assert hasattr(BaseCollection, "__init__")
    assert hasattr(BaseCollection, "__str__")
