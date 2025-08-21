This Python script will implement a Library Management System using a MySQL database to efficiently manage books and shelves (genres). I will connect to a MySQL database named library_db, creating tables for shelves and books if they don’t exist. Shelves will be uniquely identified by name, and books will be linked to shelves via foreign keys.

I will add new shelf categories (genres) to organize books better. I will support adding books with details like title, author, ISBN, quantity, and associated shelf, creating the shelf automatically if it doesn't exist.

Users will be able to list all books alphabetically or search by title, author, or ISBN. The system will manage book inventory by reducing quantity when books are borrowed and increasing it when returned, ensuring availability before lending.

An admin mode, protected by a password, will let users manage the library, including adding, borrowing, and returning books. The script will run in a loop, presenting a menu for finding books, accessing admin mode, or exiting.

Overall, this system will provide a simple, interactive way to manage library books and categories, track available copies, and facilitate borrowing and returning through a console interface connected to a MySQL backend.
