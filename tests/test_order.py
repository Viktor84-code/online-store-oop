"""Тесты для класса Order."""

from src import LawnGrass, Order, Product, Smartphone


def test_order_creation():
    """Тест создания заказа с Product."""
    product = Product("Тестовый товар", 1000.0, "Описание", 10)
    order = Order("Тестовый заказ", "Описание заказа", product, 3)

    assert order.name == "Тестовый заказ"
    assert order.description == "Описание заказа"
    assert order.product == product
    assert order.quantity == 3
    assert order.total_price == 3000.0


def test_order_with_smartphone():
    """Тест создания заказа со смартфоном."""
    phone = Smartphone("iPhone 15", 100000.0, "Флагман", 5, 95.5, "15", 512, "Black")
    order = Order("Заказ iPhone", "Срочный заказ", phone, 2)

    assert order.product.name == "iPhone 15"
    assert order.total_price == 200000.0


def test_order_with_lawngrass():
    """Тест создания заказа с травой."""
    grass = LawnGrass(
        "Газон элитный", 500.0, "Для газона", 20, "Россия", "7 дней", "Зелёный"
    )
    order = Order("Заказ травы", "Для участка", grass, 10)

    assert order.product.name == "Газон элитный"
    assert order.total_price == 5000.0


def test_order_str():
    """Тест строкового представления заказа."""
    product = Product("Книга", 500.0, "Интересная", 15)
    order = Order("Книжный заказ", "Подарок", product, 2)

    expected = "Заказ: Книжный заказ\nТовар: Книга\nКоличество: 2\nСумма: 1000.0 руб."
    assert str(order) == expected
