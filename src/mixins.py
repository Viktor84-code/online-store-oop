"""Миксины для классов."""


class PrintMixin:
    """Миксин для печати информации о создании объекта."""

    def __init__(self, *args, **kwargs):
        """
        Выводит информацию о создании объекта.

        Формат: Название класса(параметры)
        """
        # Собираем параметры для красивого вывода
        params = ", ".join(repr(arg) for arg in args)
        if kwargs:
            params += ", " + ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())

        print(f"{self.__class__.__name__}({params})")

        # Вызываем следующий __init__ в цепочке MRO
        super().__init__(*args, **kwargs)
