class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = "available"  

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def search_books(self, search):
        results = [book for book in self.books if search.lower() in book.title.lower() or search.lower() in book.author.lower()]
        if results:
            print("Search results:")
            for book in results:
                print(f" - {book}")
        else:
            print("No books found matching your search.")

    def mark_issued(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "available":
                    book.status = "issued"
                    print(f"Book '{book.title}' has been issued.")
                else:
                    print(f"Book '{book.title}' is already issued.")
                return
        print(f"No book found with ISBN {isbn}.")

    def mark_returned(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "issued":
                    book.status = "available"
                    print(f"Book '{book.title}' has been returned.")
                else:
                    print(f"Book '{book.title}' is already available.")
                return
        print(f"No book found with ISBN {isbn}.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library books:")
            for book in self.books:
                print(f" - {book}")

if __name__ == "__main__":
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "12345")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "67890")
    book3 = Book("1984", "George Orwell", "54321")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.display_books()

    library.search_books("George")

    library.mark_issued("54321")

    library.mark_issued("54321")

    library.mark_returned("54321")

    library.mark_returned("54321")

    library.display_books()