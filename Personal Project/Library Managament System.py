class Library: # Class as library
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books.append(book_name) #adds book to list
            print(f'"{book_name}" has been added to the library.')
        else:
            print(f'"{book_name}" is already in the library.') #prints this if book already declared in list

    def remove_book(self, book_name): #removing a exsisting book from a list
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'"{book_name}" has been removed from the library.')
        else:
            print(f'"{book_name}" is not in the library.')

    def display_books(self): #displaying all the books in the list
        if self.books:
            print("Books currently in the library:")
            for book in self.books:
                print(f"- {book}")

def main():
    library = Library() #main method

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")
        choice = input("Enter your choice (1-4):")
        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '2':
            book_name = input("Enter the name of the book to remove: ")
            library.remove_book(book_name)
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

