class Book:
    def __init__(self, title="", author="", pages=""):
        self.set_title(title) # titre du livre
        self.set_author(author) # auteur
        self.set_pages(pages) # nombre de pages

    def set_title(self, title: str):
        if title:
            self.title = title
        else:
            print("The title should be exist")
            self.title = "NOT FOUND"

    def set_author(self, author: str):
        if author:
            self.author = author
        else:
            print("The author should be exist")
            self.author = "NOT FOUND"

    def set_pages(self, pages: int):
        if pages:
            self.pages = pages
        else:
            print("The pages should be exist")
            self.pages = "NOT FOUND"


    def __repr__(self):
        return f"Title : {self.title}\nAuthor : {self.author}\nPages : {self.pages}\n"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
    
    def get_all_books(self):
        return [book for book in self.books]

    def remove_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"The book with the title '{title}' is removed successfuly!\n")
                return
        print("The book doesn't exist in the list!\n")

    def find_book_by_author(self, author):
        books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                books.append(book)
        if books:
            print(f"The book(s) you're looking for is/are : \n")
            for the_book in books:
                print(the_book)
        else:
            print("There is no book in the list!\n")

    def show_books(self):
        return [print(f"Book number {i+1} :\n{book}") for i, book in enumerate(self.books)]

library = Library()
book1 = Book("How to improve your Chess tactics", "Hassan BENBRIK", 231)
book2 = Book("Master the endgames", "Hassan BENBRIK", 172)
book3 = Book("My Book", "Hassan", 83)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

library.find_book_by_author("Hassan BENBRIK")

library.remove_book_by_title("Master the endgames")
library.remove_book_by_title("How to improve your Chess tactics")

library.show_books()

library.find_book_by_author("Hassan BENBRIK")
