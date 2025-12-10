import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


def test_product_default_values():
    """Тест значений по умолчанию (если есть)."""
    product = Product("Товар", "Описание", 500.0, 10)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, (int, float))
    assert isinstance(product.quantity, int)
