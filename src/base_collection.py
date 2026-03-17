"""Абстрактный базовый класс для коллекций (категории, заказы)."""

from abc import ABC, abstractmethod


class BaseCollection(ABC):
    """Абстрактный базовый класс для коллекций."""

    @abstractmethod
    def __init__(self, name, description):
        """Инициализация коллекции с названием и описанием."""
        pass

    @abstractmethod
    def __str__(self):
        """Строковое представление коллекции."""
        pass
