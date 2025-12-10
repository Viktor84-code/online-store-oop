import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
