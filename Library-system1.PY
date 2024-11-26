class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book_name, copies=1):
        if book_name in self.books:
            self.books[book_name] += copies
        else:
            self.books[book_name] = copies
        print(f"'{book_name}' added with {copies} copies.")
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nAvailable Books:")
            for book, copies in self.books.items():
                print(f"  - {book} ({copies} copies)")
    
    def borrow_book(self, book_name):
        if book_name in self.books and self.books[book_name] > 0:
            self.books[book_name] -= 1
            print(f"You have borrowed '{book_name}'.")
        elif book_name in self.books:
            print(f"'{book_name}' is currently out of stock.")
        else:
            print(f"'{book_name}' is not available in the library.")
    
    def return_book(self, book_name):
        if book_name in self.books:
            self.books[book_name] += 1
        else:
            self.books[book_name] = 1
        print(f"'{book_name}' has been returned to the library.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue
        
        if choice == 1:
            book_name = input("Enter the book name: ").strip()
            try:
                copies = int(input("Enter the number of copies: "))
            except ValueError:
                print("Invalid input. Number of copies must be an integer.")
                continue
            library.add_book(book_name, copies)
        elif choice == 2:
            library.display_books()
        elif choice == 3:
            book_name = input("Enter the book name to borrow: ").strip()
            library.borrow_book(book_name)
        elif choice == 4:
            book_name = input("Enter the book name to return: ").strip()
            library.return_book(book_name)
        elif choice == 5:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()