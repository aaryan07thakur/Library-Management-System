# Library Management System

The Library Management System is a Django-based web application for managing a library's books, users, and book borrowing records.

## Setup Instructions

### 1. Prerequisites

- [Python](3.6 or higher)
- [Virtualenv]
- [MySQL] database server

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/Library-Management-System.git
cd Library-Management-System

### 3. Create and Activate Virtual Environment (Optional)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

### 4. Configure the Database Server
Update the database settings accordingly in settings.py

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate

### 6. Run the Development Server
```bash
python manage.py runserver

# API DOCUMENTATION
# Library Management System API Documentation

## User APIs

### 1. Create a New User

- **Endpoint:** `/api/create_user/`
- **Method:** POST
- **Parameters:**
  - `Name`: User's name
  - `Email`: User's email
  - `MembershipDate`: Date of membership

### 2. List All Users

- **Endpoint:** `/api/list_all_users/`
- **Method:** GET

### 3. Get User by ID

- **Endpoint:** `/api/get_user_by_id/{user_id}/`
- **Method:** GET

## Book APIs

### 1. Add a New Book

- **Endpoint:** `/api/add_new_book/`
- **Method:** POST
- **Parameters:**
  - `Title`: Book title
  - `ISBN`: International Standard Book Number
  - `PublishedDate`: Date of publication
  - `Genre`: Book genre

### 2. List All Books

- **Endpoint:** `/api/list_all_books/`
- **Method:** GET

### 3. Get Book by ID

- **Endpoint:** `/api/get_book_by_id/{book_id}/`
- **Method:** GET

### 4. Assign/Update Book Details

- **Endpoint:** `/api/assign_update_book_details/{book_id}/`
- **Method:** POST
- **Parameters:**
  - `NumberOfPages`: Number of pages in the book
  - `Publisher`: Book publisher
  - `Language`: Book language

## BorrowedBooks APIs

### 1. Borrow a Book

- **Endpoint:** `/api/borrow_book/`
- **Method:** POST
- **Parameters:**
  - `UserID`: ID of the user borrowing the book
  - `BookID`: ID of the book being borrowed
  - `BorrowDate`: Date of borrowing

### 2. Return a Book

- **Endpoint:** `/api/return_book/{borrow_id}/`
- **Method:** POST

### 3. List All Borrowed Books

- **Endpoint:** `/api/list_all_borrowed_books/`
- **Method:** GET
