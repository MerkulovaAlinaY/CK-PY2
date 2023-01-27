class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Дочерний класс"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                AttributeError('pages должен быть положительным числом')
        else:
            AttributeError('pages должен быть типа int')

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        repr_super = super().__repr__()
        return f"{repr_super}"


class AudioBook(Book):
    """Дочерний класс"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                AttributeError('duration должен быть положительным числом')
        else:
            AttributeError('duration должен быть типа float')

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Продолжительность: {self.duration}"

    def __repr__(self):
        repr_super = super().__repr__()
        return f"{repr_super}"


if __name__ == "__main__":
    a = AudioBook("Академия", "Айзек Азимов", 504.4)
    b = PaperBook("Противостояние", "Стивен Кинг", 810)
    print(a)
    print(b)
    print(repr(a))
    print(repr(b))
