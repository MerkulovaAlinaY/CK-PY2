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

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_}, name={self.name}, pages={self.pages})"


class Library:
    def __init__(self, books: list[Book] = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self, id_):
        if len(self.books) == 0:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        for i, books in enumerate(BOOKS_DATABASE):
            if "id" in books and books["id"] == id_:
                return i
            else:
                return ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id(1))  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id(1))  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
