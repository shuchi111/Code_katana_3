class Library:
    def _init_(self):
        self.books = []
        self.members = []

    def addBook(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def borrowBook(self, book, member):
        if book in self.books:
            if not book.borrowed:
                book.borrowed = True
                member.borrowed_books.append(book)
                print(f"Book '{book.title}' has been borrowed by {member.name}.")
            else:
                print(f"Book '{book.title}' is already borrowed by someone else.")
        else:
            print(f"Book '{book.title}' is not available in the library.")

class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

class Member:
    def _init_(self, name):
        self.name = name
        self.borrowed_books = []

