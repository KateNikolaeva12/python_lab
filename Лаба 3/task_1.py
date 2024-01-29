class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int) and pages > 0:
            self.pages = pages
        else:
            raise TypeError("Количество страниц должно указываться в положительных целых числах")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, (float, int)) and duration > 0:
            self.duration = duration
        else:
            raise TypeError("Длительность книги должна указываться положительным числом")

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Длительность {self.__author} часов"
    # Длительность скорее всего лучше хранить в часах, но для небольших книг можно прописать особую логику

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r}, duration={self.duration})"