class Book:
    book_id_counter = 0
    def __init__(self, title="", author="", pages=""):
        self.book_id = self.get_book_id()
        self.set_title(title) # titre du livre
        self.set_author(author) # auteur
        self.set_pages(pages) # nombre de pages
        self.is_borrowed  = False # emprunter

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
    
    @classmethod
    def get_book_id(cls):
        cls.book_id_counter += 1
        return cls.book_id_counter

    def __repr__(self):
        return f"Title : {self.title}\nAuthor : {self.author}\nPages : {self.pages}\n"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
    
    def get_all_books(self):
        return [book for book in self.books]
    
    def is_available(self, book):
        return book in self.books

    # def remove_book_by_id(self, id):
    #     for book in self.books:
    #         if book.id == id:
    #             self.books.remove(book)
    #             print(f"The book with the id '{id}' is removed successfuly!\n")
    #             return
    #     print("The book doesn't exist in the list!\n")

    def remove_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"The book with the title :'{title}' is removed successfuly!\n")
                return
        print("The book doesn't exist in the list!\n")

    # def remove_book_by_author(self, author):
    #     for book in self.books:
    #         if book.author.lower() == author.lower():
    #             self.books.remove(book)
    #             print(f"The book with the author '{author}' is removed successfuly!\n")
    #             return
    #     print("The book doesn't exist in the list!\n")




    # def find_book_by_id(self, id):
    #     books = []
    #     for book in self.books:
    #         if book.id == id:
    #             books.append(book)
    #     if books:
    #         print(f"The book(s) you're looking for is/are : \n")
    #         for the_book in books:
    #             print(the_book)
    #     else:
    #         print("There is no book in the list!\n")

    # def find_book_by_title(self, title):
    #     books = []
    #     for book in self.books:
    #         if book.title.lower() == title.lower():
    #             books.append(book)
    #     if books:
    #         print(f"The book(s) you're looking for is/are : \n")
    #         for the_book in books:
    #             print(the_book)
    #     else:
    #         print("There is no book in the list!\n")

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




    def borrow_book_by_id(self, id):
        for book in self.books:
            if (book.id == id) and self.is_available(book):
                if book.is_borrowed == False:
                    book.is_borrowed = True
                    print(f"You have successfuly borrowed the book with the id : '{id}'\n")
                    return
                else:
                    print(f"Sorry, the book with the id : '{id}' is not available!\n")
                    return
        print(f"The book with the id : {id} is either removed or the id is wrong\n")

    def return_book_by_id(self, id):
        for book in self.books:
            if (book.id == id) and self.is_available(book):
                if book.is_borrowed == True:
                    book.is_borrowed = False
                    print(f"You have successfuly returned the book with the id : '{id}'\n")
                    return
                else:
                    print(f"The book with the id : '{id}' was not borrowed\n")
                    return
        print(f"The book with the id : {id} is either removed or the id is wrong\n")

    def borrow_book_by_title(self, title):
        for book in self.books:
            if (book.title.lower() == title.lower()) and self.is_available(book):
                if book.is_borrowed == False:
                    book.is_borrowed = True
                    print(f"You have successfuly borrowed the book with the title : '{title}'\n")
                    return
                else:
                    print(f"Sorry, the book with the title : '{title}' is not available!\n")
                    return
        print(f"The book with the title : {title} is either removed or the title is wrong\n")

    def return_book_by_title(self, title):
        for book in self.books:
            if (book.title.lower() == title.lower()) and self.is_available(book):
                if book.is_borrowed == True:
                    book.is_borrowed = False
                    print(f"You have successfuly returned the book with the title : '{title}'\n")
                    return
                else:
                    print(f"The book with the title : '{title}' was not borrowed\n")
                    return
        print(f"The book with the title : {title} is either removed or the title is wrong\n")


library = Library()
book1 = Book("How to improve your Chess tactics", "Hassan BENBRIK", 231)
book2 = Book("Master the endgames", "Hassan BENBRIK", 172)
book3 = Book("How to create an app using OOP", "Moussa Jamor", 83)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

library.find_book_by_author("Hassan BENBRIK")

library.remove_book_by_title("Master the endgames")
# library.remove_book_by_title("How to improve your Chess tactics")

library.show_books()

library.find_book_by_author("Hassan BENBRIK")


library.find_book_by_author("Moussa Jamor")

library.return_book_by_title("Master the endgames")
library.borrow_book_by_title("Master the endgames")
