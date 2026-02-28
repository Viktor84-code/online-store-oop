import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from src.product import Product


def test_product_creation():
    """Тест создания продукта."""
    product = Product(
        name="Тестовый товар",
        description="Тестовое описание",
        price=1000.0,
        quantity=5
    )

    assert product.name == "Тестовый товар"
    assert product.description == "Тестовое описание"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_price_setter_positive():
    """Тест установки положительной цены"""
    product = Product("iPhone", 100000, "Флагман", 5)
    product.price = 150000
    assert product.price == 150000


def test_price_setter_negative(capsys):
    """Тест установки отрицательной цены (должен печатать сообщение)"""
    product = Product("iPhone", 100000, "Флагман", 5)
    product.price = -50

    captured = capsys.readouterr()
    assert "не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 100000  # Цена не изменилась


def test_new_product():
    """Тест создания продукта из словаря"""
    data = {
        "name": "Xiaomi",
        "price": 30000,
        "description": "Смартфон",
        "quantity": 10
    }
    product = Product.new_product(data)

    assert product.name == "Xiaomi"
    assert product.price == 30000
    assert product.description == "Смартфон"
    assert product.quantity == 10


def test_new_product_with_check_new():
    """Тест создания нового продукта (без дубликатов)"""
    existing = []
    data = {"name": "Xiaomi", "price": 30000, "description": "Смартфон", "quantity": 10}

    product = Product.new_product_with_check(data, existing)

    assert product.name == "Xiaomi"
    assert product.quantity == 10


def test_new_product_with_check_duplicate():
    """Тест создания дубликата (должен обновить существующий)"""
    existing = [Product("Xiaomi", 30000, "Смартфон", 10)]
    data = {"name": "Xiaomi", "price": 35000, "description": "Смартфон", "quantity": 5}

    product = Product.new_product_with_check(data, existing)

    assert product is existing[0]  # Тот же объект
    assert product.quantity == 15  # Количество сложилось
    assert product.price == 35000  # Цена взята большая


def test_str_method():
    """Тест строкового представления"""
    product = Product("iPhone", 100000, "Флагман", 5)

    assert str(product) == "iPhone, 100000 руб. (остаток: 5)"

def test_set_price_with_confirmation_higher(monkeypatch):
    """Тест повышения цены (без подтверждения)"""
    product = Product("Товар", 100, "Описание", 5)  # name, price, description, quantity
    product.set_price_with_confirmation(150)
    assert product.price == 150
