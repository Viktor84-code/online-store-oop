"""Тесты для миксинов."""

from src import Product, Smartphone, LawnGrass


def test_print_mixin_product(capsys):
    """Тест, что миксин печатает информацию о создании Product."""
    Product("TestProduct", 1000.0, "Test Description", 10)  # ← без переменной!
    captured = capsys.readouterr()
    assert "Product('TestProduct', 1000.0, 'Test Description', 10)" in captured.out


def test_print_mixin_smartphone(capsys):
    """Тест, что миксин работает для Smartphone (только базовые параметры)."""
    Smartphone(
        "TestPhone", 50000.0, "Test Smartphone", 5, 95.5, "X100", 128, "Black"
    )  # ← без переменной!
    captured = capsys.readouterr()
    assert "Smartphone('TestPhone', 50000.0, 'Test Smartphone', 5)" in captured.out


def test_print_mixin_lawngrass(capsys):
    """Тест, что миксин работает для LawnGrass (только базовые параметры)."""
    LawnGrass(
        "TestGrass", 300.0, "Test Grass", 20, "Russia", "10 days", "Green"
    )  # ← без переменной!
    captured = capsys.readouterr()
    assert "LawnGrass('TestGrass', 300.0, 'Test Grass', 20)" in captured.out


def test_print_mixin_multiple_objects(capsys):
    """Тест, что миксин печатает для каждого созданного объекта."""
    Product("P1", 100, "Desc1", 1)
    Product("P2", 200, "Desc2", 2)
    captured = capsys.readouterr()

    assert "Product('P1', 100, 'Desc1', 1)" in captured.out
    assert "Product('P2', 200, 'Desc2', 2)" in captured.out


def test_mixin_print(capsys):
    Product("Test", 100, "Desc", 5)
    captured = capsys.readouterr()
    assert "Product" in captured.out

