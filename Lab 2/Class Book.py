BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            return TypeError("id книги должно быть типа int")
        if id_ < 0:
            return ValueError("id книги должно быть положительным числом")
        self.id_ = id_
        if not isinstance(name, str):
            return TypeError("Имя должно быть типа str")
        self.name = name
        if not isinstance(pages, int):
            return TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            return ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)


    print(list_books)
