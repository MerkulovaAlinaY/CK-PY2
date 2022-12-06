import doctest


class Star:
    def __int__(self, mass: float, luminosity: float):
        """
        Создание и подготовка к работе объекта "Звезда"
        :param mass: Масса звезды, в кг
        :param luminosity: Светимость звезды, в эрг
        Примеры:
        >>> star = Star(10**30, 10**33)  # инициализация экземпляра класса
        """
        if not isinstance(mass, (int, float)):
            raise TypeError("Масса звезды должна быть типа int или float")
        if mass <= 0:
            raise ValueError("Масса звезды должна быть положительным числом")
        self.mass = mass

        if not isinstance(luminosity, (int, float)):
            raise TypeError("Светимость звезды должна быть типа int или float")
        if luminosity <= 0:
            raise ValueError("Светимость звезды должна быть положительным числом")
        self.luminosity = luminosity

    def star_in_sky(self) -> bool:
        """
        Проверяет находится звезда на небе или нет
        :return: Находится ли звезда на небе
        Пример:
        >>>star = Star(10**30, 10**33)
        >>>star.star_in_sky()
        """
        ...

    def velocity(self, luch_velocity: float) -> float:
        """
        Определяет пространственную скорость звезды, учитывая ее лучевую скорость
        :param luch_velocity: лучевая скорость звезды, в км/с
        :return: Пространственную скорость звезды
        Пример:
        >>>star = Star(10**30, 10**33)
        >>>star.velocity(245)
        """
        if not isinstance(luch_velocity, (int, float)):
            raise TypeError("Лучевая скорость звезды должна быть типа int или float")
        if luch_velocity <= 0:
            raise ValueError("Лучевая скорость звезды должна быть положительным числом и не может равняться 0")
        ...


class Cake:
    def __int__(self, capacity: float, weight: float):
        """
        Создание и подготовка к работе объекта "Торт"
        :param capacity: Объем торта
        :param weight: Вес торта
        Примеры:
        >>> cake = Cake(300, 2)  # инициализация экземпляра класса
        """
        if not isinstance(capacity, (int, float)):
            raise TypeError("Объем торта должен быть типа str")
        if capacity <= 0:
            raise ValueError("Объем торта должен быть положительным числом")
        self.capacity = capacity

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес торта должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес торта должен быть положительным числом")
        self.weight = weight

    def change_weight(self, piece) -> float:
        """"
        Уменьшает вес торта путем отрезания какой то части
        :raise ValueError: Если вес отрезаемой части больше веса торта, то возвращается ошибка
        :return: Новый вес торта
        Пример:
        >>>cake = Cake(300, 2)
        >>>cake.change_weight(0.3)
        """
        if not isinstance(piece, (int, float)):
            raise TypeError("Отрезамая часть должна быть типа int или float")
        if piece < 0:
            raise ValueError("Отрезамая часть должна быть положительным числом")
        ...

    def taste_cake(self) -> bool:
        """"
        Метод опеределяет является ли торт вкусным
        :return: Является ли торт вкусным
        Пример:
        >>>cake = Cake(300, 2)
        >>>cake.taste_cake()
        """
        ...


class Movie:
    def __int__(self, name: str, year: int):
        """
        Создание и подготовка к работе объекта "Фильм"
        :param name: Название фильма, может содержать любые символы, буквы и цифры
        :param year: год выпуска
        Пример:
        >>>movie = Movie("1917", 2019) # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название фильма должно быть типа str")
        self.name = name

        if not isinstance(year, int):
            raise TypeError("Год выпуска фильма должен быть типа int")
        if year < 1896:
            raise ValueError(
                "Первый фильм в истории появился 28 декабря 1895 года, год выпуска должен быть больше 1895")
        self.year = year

    def do_rating(self, evaluation: int) -> float:
        """
        Формирует рейтинг фильма
        :param evaluation: Оценка фильма по мнению пользователя
        :return: Рейтинг фильма на основе оценок
        Пример:
        >>>movie = Movie("1917", 2019)
        >>>movie.do_rating(8)
        """
        if not isinstance(evaluation, int):
            raise TypeError("Оценка должна быть типа int")
        if 0 > evaluation > 10:
            raise ValueError("Оценка должна быть положительным числом и не больше 10")
        ...

    def watch_movie(self) -> bool:
        """
        Метод опеределяет просмотре фильма
        :return: Просмотрен ли фильм
        Пример:
        >>>movie = Movie("1917", 2019)
        >>>movie.watch_movie()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()