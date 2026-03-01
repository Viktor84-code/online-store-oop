import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.category import Category
from src.product import Product


def test_category_creation():
    """Тест создания категории."""
    product = Product("Товар", "Описание", 100.0, 5)
    category = Category("Категория", "Описание категории", [product])

    assert category.name == "Категория"
    assert category.description == "Описание категории"
    assert len(category.products) == 1
    assert category.products[0].name == "Товар"


def test_category_counters():
    """Тест счётчиков категорий и продуктов."""
    # Сбросим счётчики для чистоты теста
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Товар 1", "Описание", 100.0, 1)
    product2 = Product("Товар 2", "Описание", 200.0, 2)

    category1 = Category("Категория 1", "Описание", [product1, product2])
    assert Category.category_count == 1
    assert Category.product_count == 2

    product3 = Product("Товар 3", "Описание", 300.0, 3)
    category2 = Category("Категория 2", "Описание", [product3])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_empty_category():
    """Тест создания категории без продуктов."""
    category = Category("Пустая категория", "Описание", [])
    assert category.name == "Пустая категория"
    assert len(category.products) == 0


def test_add_product():
    """Тест добавления продукта"""
    category = Category("Смартфоны", "Телефоны", [])
    product = Product("iPhone", 100000, "Флагман", 5)

    category.add_product(product)

    assert len(category._products) == 1
    assert Category.product_count > 0


def test_add_product_wrong_type():
    """Тест добавления не-Product"""
    category = Category("Смартфоны", "Телефоны", [])

    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_products_property():
    """Тест геттера products"""
    product = Product("iPhone", 100000, "Флагман", 5)
    category = Category("Смартфоны", "Телефоны", [product])

    assert isinstance(category.products, list)
    assert category.products[0] == product


def test_get_products_display():
    """Тест форматированного вывода"""
    product = Product("iPhone", 100000, "Флагман", 5)
    category = Category("Смартфоны", "Телефоны", [product])

    display = category.get_products_display()
    assert "iPhone" in display
    assert "100000 руб." in display
    assert "Остаток: 5 шт." in display


def test_products_count():
    """Тест счетчика продуктов"""
    product1 = Product("iPhone", 100000, "Флагман", 5)
    product2 = Product("Samsung", 80000, "Флагман", 3)
    category = Category("Смартфоны", "Телефоны", [product1, product2])

    assert category.products_count == 2
