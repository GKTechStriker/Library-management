import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GkartikG",
    database="library_db"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Function to initialize the database (create tables if they don't exist)
def initialize_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS shelves (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) UNIQUE)")
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), isbn VARCHAR(13) UNIQUE, quantity INT, shelf_id INT, FOREIGN KEY (shelf_id) REFERENCES shelves(id))")
    db.commit()

# Function to add a new shelf (genre)
def add_shelf(shelf_name):
    query = "INSERT INTO shelves (name) VALUES (%s)"
    cursor.execute(query, (shelf_name,))
    db.commit()
    print(f"Shelf '{shelf_name}' added successfully!")

# Function to add a book to the appropriate shelf
def add_book(title, author, isbn, quantity, shelf_name):
    # Check if the shelf exists
    cursor.execute("SELECT id FROM shelves WHERE name = %s", (shelf_name,))
    shelf = cursor.fetchone()
    
    if not shelf:
        print(f"Shelf '{shelf_name}' does not exist. Creating it now...")
        add_shelf(shelf_name)
        cursor.execute("SELECT id FROM shelves WHERE name = %s", (shelf_name,))
        shelf = cursor.fetchone()
    
    shelf_id = shelf[0]
    
    query = "INSERT INTO books (title, author, isbn, quantity, shelf_id) VALUES (%s, %s, %s, %s, %s)"
    values = (title, author, isbn, quantity, shelf_id)
    
    try:
        cursor.execute(query, values)
        db.commit()
        print("Book added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to list all books in alphabetical order by title
def list_books():
    query = "SELECT books.id, books.title, books.author, books.isbn, books.quantity, shelves.name FROM books JOIN shelves ON books.shelf_id = shelves.id ORDER BY books.title ASC"
    
    cursor.execute(query)
    books = cursor.fetchall()
    
    if not books:
        print("No books found.")
    else:
        for book in books:
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("ISBN:", book[3])
            print("Quantity:", book[4])
            print("Shelf:", book[5])
            print("--------------------------")

# Function to find a book by title, author, or ISBN
def find_book(search_term):
    query = "SELECT books.id, books.title, books.author, books.isbn, books.quantity, shelves.name FROM books JOIN shelves ON books.shelf_id = shelves.id WHERE books.title LIKE %s OR books.author LIKE %s OR books.isbn = %s"
    cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", search_term))
    books = cursor.fetchall()
    
    if not books:
        print("No matching books found.")
    else:
        for book in books:
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("ISBN:", book[3])
            print("Quantity:", book[4])
            print("Shelf:", book[5])
            print("--------------------------")

# Function to borrow a book (reduce quantity)
def borrow_book(book_id):
    query = "UPDATE books SET quantity = quantity - 1 WHERE id = %s AND quantity > 0"
    cursor.execute(query, (book_id,))
    db.commit()
    
    if cursor.rowcount > 0:
        print("Book borrowed successfully!")
    else:
        print("Book not available or invalid ID.")

# Function to return a book (increase quantity)
def return_book(book_id):
    query = "UPDATE books SET quantity = quantity + 1 WHERE id = %s"
    cursor.execute(query, (book_id,))
    db.commit()
    
    if cursor.rowcount > 0:
        print("Book returned successfully!")
    else:
        print("Invalid book ID.")

# Admin Mode
def admin_mode():
    pwd=input("Enter Password:")
    
    if pwd=="loge":
        print("\nAdmin Mode")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit Admin Mode")
        
        choice = input("Enter your choice: ")
        
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            quantity = int(input("Enter quantity: "))
            shelf_name = input("Enter shelf name (genre): ")
            add_book(title, author, isbn, quantity, shelf_name)
        
        elif choice == "2":
            book_id = int(input("Enter book ID to borrow: "))
            borrow_book(book_id)
        
        elif choice == "3":
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)
        
        elif choice == "4":
            start()

        else:
            print("Invalid choice!, Try again.")
            admin_mode()
    else:
        print("wrong Password:")
        print("1).Retype Password")
        print("2).Exit Admin Mode")
        png=input("Enter your choice:")
        if png=="1":
            admin_mode()
        elif png=="2":
            start()
# Main Program
initialize_database()
def start():
    print("\nLibrary Management System")
    print("1. find Book")
    print("2. Admin Mode")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        st=input("Type Book title, author, or ISBN:")
        find_book(st)
    elif choice == "2":
        admin_mode()
    elif choice == "3":
        print("Exit successful.")
    else:
        print("Invalid choice!, try again")
        start()
# Close the database connection
db.close()
start()
