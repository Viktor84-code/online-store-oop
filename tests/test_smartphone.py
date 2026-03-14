from src import Smartphone


def test_smartphone_creation():
    """Тест создания смартфона с доп. атрибутами"""
    phone = Smartphone(
        "iPhone 15", 210000.0, "512GB, Gray space", 8, 98.2, "15", 512, "Gray space"
    )

    assert phone.name == "iPhone 15"
    assert phone.price == 210000.0
    assert phone.description == "512GB, Gray space"
    assert phone.quantity == 8
    assert phone.efficiency == 98.2
    assert phone.model == "15"
    assert phone.memory == 512
    assert phone.color == "Gray space"


def test_smartphone_str():
    """Тест строкового представления смартфона (наследуется от Product)"""
    phone = Smartphone("iPhone 15", 210000.0, "512GB", 8, 98.2, "15", 512, "Gray")
    assert str(phone) == "iPhone 15, 210000.0 руб. Остаток: 8 шт."
