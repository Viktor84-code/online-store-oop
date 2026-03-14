"""Тесты для миксинов."""

import pytest
from src import Product, Smartphone, LawnGrass


def test_print_mixin_product(capsys):
    """Тест, что миксин печатает информацию о создании Product."""
    product = Product("TestProduct", 1000.0, "Test Description", 10)
    captured = capsys.readouterr()
    assert "Product('TestProduct', 1000.0, 'Test Description', 10)" in captured.out


def test_print_mixin_smartphone(capsys):
    """Тест, что миксин работает для Smartphone."""
    phone = Smartphone("TestPhone", 50000.0, "Test Smartphone", 5, 95.5, "X100", 128, "Black")
    captured = capsys.readouterr()
    # Миксин печатает только то, что передано в super().__init__
    assert "Smartphone('TestPhone', 50000.0, 'Test Smartphone', 5)" in captured.out


def test_print_mixin_lawngrass(capsys):
    """Тест, что миксин работает для LawnGrass."""
    grass = LawnGrass("TestGrass", 300.0, "Test Grass", 20, "Russia", "10 days", "Green")
    captured = capsys.readouterr()
    # Проверяем только базовые параметры!
    assert "LawnGrass('TestGrass', 300.0, 'Test Grass', 20)" in captured.out


def test_print_mixin_multiple_objects(capsys):
    """Тест, что миксин печатает для каждого созданного объекта."""
    p1 = Product("P1", 100, "Desc1", 1)
    p2 = Product("P2", 200, "Desc2", 2)
    captured = capsys.readouterr()

    assert "Product('P1', 100, 'Desc1', 1)" in captured.out
    assert "Product('P2', 200, 'Desc2', 2)" in captured.out
