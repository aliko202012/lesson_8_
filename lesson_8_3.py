import sqlite3

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def add_book(self, book):
        self.cursor.execute('''
            INSERT INTO books (title, author, year) VALUES (?, ?, ?)
        ''', (book.title, book.author, book.year))
        self.conn.commit()

    def find_book_by_title(self, title):
        self.cursor.execute('''
            SELECT title, author, year FROM books WHERE LOWER(title) = LOWER(?)
        ''', (title,))
        book_data = self.cursor.fetchone()
        if book_data:
            return Book(*book_data)
        return None

    def list_books(self):
        self.cursor.execute('SELECT title, author, year FROM books')
        return [Book(*row) for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()

library = Library()


library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))


search_title = "1984"
found_book = library.find_book_by_title(search_title)
if found_book:
    print(f"Найдена книга: {found_book.title} by {found_book.author}, {found_book.year}")
else:
    print(f"Книга с названием '{search_title}' не найдена.")

print("\nСписок всех книг в библиотеке:")
for book in library.list_books():
    print(f"{book.title} by {book.author}, {book.year}")

library.close()