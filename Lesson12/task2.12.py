# Task 2
# Library

# Write a class structure that implements a library.Classes :
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author(author must be an instance of Author class )
# 3) Author - name, country, birthday, books =[]
# Library class Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book
# class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing boock
class Author:

    def __init__(self, author_name: str, country: str, birthday: int):
        self.author_name = author_name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.author_name} is author from {self.country}.' \
               f' Was born in {self.birthday}th.'

    def new_author_book(self, name: str, year: int):
        book = Book(name, year, self)
        self.books.append(book)
        return book


class Book:

    def __init__(self, book_name: str, year: int, author: Author):
        self.book_name = book_name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.book_name} was writen in {self.year} by {self.author.author_name}'


class Library:
    my_library = ''

    def __init__(self, name):
        self.name = name
        self.books = []
        self.author = []

    def new_book(self, book: Book):
        self.books.append(book)
        return book

    def get_author(self):
        return set([book.author for book in self.books])

    def group_by_author(self, author: Author):
        return [book.book_name for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book.book_name for book in self.books if book.year == year]


if __name__ == '__main__':
    author1 = Author('Thomas Harris', 'USA', 1940)
    author2 = Author('Stephan King', 'USA', 1947)

    book1 = Book('Hannibal', 1999, author1)
    book2 = Book('Dark Tower:The Gunslinger', 1982, author2)
    book3 = Book('Under the dome', 2009, author2)
    print(book1.author)

    book4 = author1.new_author_book('The green mile', 1996)
    print(book4.book_name)

    my_library1 = Library('Bernes&Noble')
    my_library1.new_book(book1)
    my_library1.new_book(book2)
    my_library1.new_book(book3)

    print(my_library1.get_author())
    print(my_library1.group_by_author(author2))
    print(my_library1.group_by_year(1999))
