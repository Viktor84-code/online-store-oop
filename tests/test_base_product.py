"""Тесты для абстрактного базового класса BaseProduct."""

import pytest

from src.base_product import BaseProduct
from src.product import Product


def test_base_product_abstract():
    """Проверка, что нельзя создать экземпляр BaseProduct."""
    with pytest.raises(TypeError):
        BaseProduct("Test", 100, "Desc", 5)


def test_product_inherits_base():
    """Проверка, что Product является наследником BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_product_implements_abstract_methods():
    """Проверка, что Product реализует все абстрактные методы."""
    # Создаём объект для тестирования (как в продакшене!)
    product = Product("TestProduct", 1000.0, "Test Description", 10)

    # Проверяем __init__
    assert product.name == "TestProduct"
    assert product.price == 1000.0
    assert product.description == "Test Description"
    assert product.quantity == 10

    # Проверяем __str__
    assert str(product) == "TestProduct, 1000.0 руб. Остаток: 10 шт."

    # Проверяем __add__
    product2 = Product("TestProduct2", 500.0, "Test Description 2", 5)
    assert product + product2 == (1000.0 * 10) + (500.0 * 5)

    # Проверяем price property
    assert product.price == 1000.0
    product.price = 1200.0
    assert product.price == 1200.0


def test_base_product_method_signatures():
    """Проверка, что абстрактные методы объявлены правильно."""
    assert hasattr(BaseProduct, "__init__")
    assert hasattr(BaseProduct, "__str__")
    assert hasattr(BaseProduct, "__add__")
    assert hasattr(BaseProduct, "price")

    # Проверяем, что price является property
    price_attr = getattr(BaseProduct, "price")
    assert isinstance(price_attr, property)


def test_base_product_abstract_methods():
    """Тест, что нельзя создать экземпляр BaseProduct"""
    with pytest.raises(TypeError):
        BaseProduct("Test", 100, "Desc", 5)


def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Test", 100, "Desc", 5)

