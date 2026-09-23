# Book Class
class Book:
 
    def __init__(self, book_id, book_name, author):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.is_borrowed = False     

    def display(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        print("Book ID :", self.book_id)
        print("Book Name :", self.book_name)
        print("Author :", self.author)
        print("Status :", status)
        print()



class Patron:

   
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []     

   
    def display(self):
        print("Patron Name :", self.name)

        if len(self.borrowed_books) == 0:
            print("Borrowed Books : None")
        else:
            print("Borrowed Books :", self.borrowed_books)

        print()



class Library:

    library_name = "MIT Library"

   
    def __init__(self):
        self.books = []
        self.patrons = []

   
    def add_book(self, book_id, book_name, author):

       
        book = Book(book_id, book_name, author)

      
        self.books.append(book)

        print("Book Added Successfully.")

   
    def register_patron(self, name):

        
        patron = Patron(name)

       
        self.patrons.append(patron)

        print("Patron Registered Successfully.")

   
    def borrow_book(self, patron_name, book_name):

        patron = None

        
        for p in self.patrons:
            if p.name == patron_name:
                patron = p

        
        for b in self.books:
            if b.book_name == book_name:
                book = b

       
        if patron and book:

            
            if book.is_borrowed == False:

                
                book.is_borrowed = True

                
                patron.borrowed_books.append(book.book_name)

                print("Book Borrowed Successfully.")

            else:
                print("Book Already Borrowed.")

        else:
            print("Book or Patron Not Found.")

   
    def return_book(self, patron_name, book_name):

        patron = None
        book = None

       
        for p in self.patrons:
            if p.name == patron_name:
                patron = p

      
        for b in self.books:
            if b.book_name == book_name:
                book = b

       
        if patron and book:

           
            if book.book_name in patron.borrowed_books:

                
                patron.borrowed_books.remove(book.book_name)

                
                book.is_borrowed = False

                print("Book Returned Successfully.")

            else:
                print("This Patron did not borrow the book.")

        else:
            print("Book or Patron Not Found.")

    
    def display_books(self):

        print("\nBooks List")

        for book in self.books:
            book.display()

    
    def display_patrons(self):

        print("\nPatron List")

        for patron in self.patrons:
            patron.display()


library = Library()

print("Library Name :", Library.library_name)


library.add_book(101, "Python", "Guido")
library.add_book(102, "Java", "James Gosling")
library.add_book(103, "C++", "Bjarne Stroustrup")


library.register_patron("Manaswi")
library.register_patron("Riya")


library.display_books()
library.display_patrons()


library.borrow_book("Manaswi", "Python")

print("\nAfter Borrowing:\n")
library.display_books()
library.display_patrons()


library.return_book("Manaswi", "Python")

print("\nAfter Returning:\n")
library.display_books()
library.display_patrons()