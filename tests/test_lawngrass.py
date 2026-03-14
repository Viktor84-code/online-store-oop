from src import LawnGrass


def test_lawngrass_creation():
    """Тест создания газонной травы с доп. атрибутами"""
    grass = LawnGrass("Газонная трава", 500.0, "Элитная трава для газона", 20, "Россия", "7 дней", "Зеленый")

    assert grass.name == "Газонная трава"
    assert grass.price == 500.0
    assert grass.description == "Элитная трава для газона"
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_lawngrass_str():
    """Тест строкового представления (наследуется от Product)"""
    grass = LawnGrass("Газонная трава", 500.0, "Элитная трава", 20, "Россия", "7 дней", "Зеленый")
    assert str(grass) == "Газонная трава, 500.0 руб. Остаток: 20 шт."


def test_lawngrass_price_setter():
    """Тест сеттера цены (наследуется от Product)"""
    grass = LawnGrass("Газонная трава", 500.0, "Элитная трава", 20, "Россия", "7 дней", "Зеленый")
    grass.price = 600.0
    assert grass.price == 600.0


def test_lawngrass_add():
    """Тест сложения двух объектов LawnGrass"""
    grass1 = LawnGrass("Трава 1", 500.0, "Описание 1", 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Трава 2", 300.0, "Описание 2", 10, "США", "5 дней", "Синий")

    result = grass1 + grass2
    expected = (500.0 * 20) + (300.0 * 10)  # 10000 + 3000 = 13000
    assert result == expected
