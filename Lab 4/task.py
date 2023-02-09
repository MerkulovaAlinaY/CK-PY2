import doctest


class Star:
    """Базовый класс"""

    def __init__(self, mass: float, temperature: float):
        """
        Создание объекта "Звезда"
        :param mass: Масса звезды, в кг
        :param temperature: Температура звезды в кельвинах
        Примеры:
        >>> star = Star(10**33, 5600)
        """
        if not isinstance(mass, (int, float)):
            raise TypeError("масса звезды должна быть типа int или float")
        if mass <= 0:
            raise ValueError("Масса звезды должна быть положительным числом")
        self.mass = mass
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура звезды должна быть типа int или float")
        if temperature <= 0:
            raise ValueError("Температура звезды должна быть положительным числом")
        self.temperature = temperature

    def __str__(self):
        return f"Звезда. Масса {self.mass}. Температура {self.temperature}"

    def __repr__(self):
        return f"{self.__class__.__name__}(mass={self.mass!r}, temperature={self.temperature!r})"


class Sun(Star):
    """Дочерний класс"""

    def __init__(self, mass: float, temperature: float, class_luminosity: str):
        """
        Подкласс объекта "Звезда" - "Солнце"
        :param mass: Масса звезды, в кг
        :param temperature: Температура звезды в кельвинах
        :param class_luminosity: Класс светимости звезды в зависимости от ее температуры
        Примеры:
        >>> star = Sun(10*33, 5000, "G")
        """
        super().__init__(mass, temperature)
        self.class_luminosity = class_luminosity

    def __call__(self, new_luminosity):
        """
        Метод производит замену класса светимости, когда звезда эволюционирует
        :param new_luminosity: новый класс светимости
        Пример
        >>> star = Sun(10*33, 5000, "G")
        >>> star("O")
        """
        self.class_luminosity = new_luminosity

    def __repr__(self):
        repr_super = super().__repr__()
        return f"({repr_super}, class_luminosity={self.class_luminosity})"

    def __str__(self):
        str_super = super().__str__()
        return f"{str_super }. Класс светимости {self.class_luminosity}"


if __name__ == "__main__":
    doctest.testmod()
    pass
