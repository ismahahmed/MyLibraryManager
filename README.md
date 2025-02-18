# MyLibraryManager

My Library Manager is a Python project that allows users to manage and explore their virtual book library. The application stores data in a CSV file (books.csv) and provides a command-line interface (CLI) to add, view, edit, delete, and sort books based on various attributes such as title, author, year of publication, ratings, genre, and read status

This project acts as a personal book database that helps users organize their books in a digital format, making it easier to track what they’ve read and what they still need to read. 

*The purpose of this project is to help me practice applying algorithms*


## Features

- View all books in the library
- Add a new book to the library
- Edit details of an existing book
- Delete a specific book from the library
- Sort books by various attributes
- Sort books within bookshelves
- Delete the entire library

```{bash}
LibraryManager/
├── data/
│   └── books.csv           # Stores book data into csv file. Each row is a different book
├── book.py                 # Contains the Book class 
├── helpers.py              # Contains helper functions like read_csv_as_dict and divide_books
├── sorting.py              # Contains sorting algorithms for books
├── validation.py           # Contains validation functions for user input
├── MyLibraryManager.py      # Main script to run the program
└── README.md               # Project documentation


MyLibraryManager/
    ├── MyLibraryManager.py
    │   ├── __init__(self, csv_file='data/books.csv')
    │   ├── view_books(self)
    │   ├── write_csv_header(self, writer)
    │   ├── write_book_to_csv(self, writer, book)
    │   ├── save_book_to_csv(self, book)
    │   ├── add_book(self)
    │   ├── delete_library(self)
    │   ├── delete_book_from_csv(self, book)
    │   ├── find_book_by_title(self, title)
    │   ├── edit_book_details(self, book)
    │   ├── update_csv_file(self)
    │   ├── edit_book(self)
    │   ├── make_sorting_choice(self)
    │   ├── menu(self)
    ├── Book.py
    │   ├── __init__(self, title, author_first, author_last, isbn, isbn13, my_rating, avg_rating, publisher, binding, num_pages, year_published, date_read, genre, age_group, read)
    │   ├── display_details(self)
    │   ├── get_book_dict(self)
    │   ├── __str__(self)
    ├── Helpers.py
    │   ├── read_csv_as_dict(csv_file)
    │   ├── divide_books(book_list)
    │   ├── rewrite_csv(csv_file, books)
    ├── Sorting.py
    │   ├── merge_sort(book_list, sorting_categories)
    │   ├── merge(left, right, sorting_categories)
    │   ├── bubble_sort_books(books, key1, key2)
    │   ├── bucket_sort_books(library)
    │   ├── print_sorted_bookshelves(library)
    ├── Validation.py
    │   ├── is_valid_date(date_str)
    │   ├── is_valid_rating(rating)
    │   ├── is_valid_age_group(age_group)
    │   ├── is_valid_num_pages(num_pages)
    │   ├── is_valid_year(year)
    │   ├── is_valid_isbn(isbn)
    │   ├── is_valid_isbn13(isbn13)
    │   ├── is_valid_binding(binding)
    └── data/
        └── books.csv
```

## Requirements

- Python version 3.x 
- `tabulate` library (this is used to display book data neatly in the CLI)

```{bash}
pip install tabulate
```

## How to Run

The csv file is currently populated with several books as examples. You can use these books to test out the different actions a user can take. Feel free to clear the library if needed using the delete library action when prompted. I suggest using this data to get comfortable with the actions availble in this program. 

To Start `My Library Manager`, run the following command

```{bash}
python MyLibraryManager.py 
```

This will open the menu where you can choose options to manage your book library. The available options are:

### 1. View Books

This option allows users to view books in a neat format

### 2. Add a Book

Allows users to enter a book into the library database (one at a time)

### 3. Edit a Book

Allows users to edit an existing book (gives users the option to edit read/not read, rating or delete the record from csv file)

### 4. Sort Books

Gives the user the option to sort and update the csv file. The user will be prompted to select from a few options on how they would like to sort the books

### 5. Print Sprted Bookshelves

Gives the user the option to view library via sorted bookshelves. Each bookshelf is a different age category: Children, Young Adult or Adult

### 6. Delete Library

Allows the user to clear library. Permanent- cannot be reversed. 

### 7. Exit

End program

## How to Add a Book

When adding a book, you will be prompted to provide the following details:

Title
Author (First Name, Last Name)
ISBN (optional)
Your Rating (optional)
Average Rating (from Goodreads)
Publisher
Binding (Paperback, Hardcover, eBook)
Number of Pages
Year Published
Date Read (if applicable)
Genre
Age Group (Children, Young Adult, Adult)

*Input validation is implemented for fields such as ISBN, ratings, year, and binding type*

## Sorting

Merge sort, a divide and conquer algorithm, is used to sort the books. Users can sort books by the following criteria:

Author Last Name, First Name + Title
Year Published + Title
Average Rating + Title
The sorted list is saved back to the books.csv file

Bucket Sort is also used to sort books within different bookshelves. These methods can be found in the sorting class

## How to Edit a Book
You can edit the following attributes of a book:

Read/Not Read & Date Read
Your Rating
Delete the book from the library
