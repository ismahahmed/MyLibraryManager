# My Library Manager

My Library Manager is a Python project that allows users to manage and explore their virtual book library. The application stores data in a CSV file (books.csv) and provides a command-line interface (CLI) to add, view, edit, delete, and sort books based on various attributes such as title, author, year of publication, ratings, genre, and read status.

This project acts as a personal book database that helps users organize their books in a digital format, making it easier to track what they’ve read and what they still need to read.

## Features

- View all books in the library
- Add a new book to the library
- Edit details of an existing book
- Delete a specific book from the library
- Sort books by various attributes
- Sort books within bookshelves
- Delete the entire library
- Estimate total reading time for unread books
- Calculate the maximum high-value books you can read within a certain time

```{bash}
LibraryManager/
├── data/
│   └── books.csv           # Stores book data into csv file. Each row is a different book
├── book.py                 # Contains the Book class 
├── helpers.py              # Contains helper functions like read_csv_as_dict and divide_books
├── sorting.py              # Contains sorting algorithms for books
├── validation.py           # Contains validation functions for user input
├── mst_clustering.py       # Contains MSTClustering class for clustering books by similarity
├── MyLibraryManager.py      # Main script to run the program
└── README.md               # Project documentation

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

Allows the user to clear library. Permanent- cannot be reversed

### 7. Estimate Total Reading Time for Unread Books
Calculates and prints the estimated time required to read all unread books in the library based on the user's reading speed

### 8. Calculate the Maximum High-Value Books I Can Read Within a Certain Time
Calculates and prints the list of books that can be read within a given time frame based on their value per hour (rating per hour)

### 9. Cluster Books by Similarity
Clusters books by similarity using MST and a greedy approach. Prompts the user for the number of clusters and prints the resulting clusters.

### 10. Exit

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

### Merge Sort (Divide and Conquer), 
Merge sort, a divide and conquer algorithm, is used to sort the books. Users can sort books by the following criteria:

Author Last Name, First Name + Title
Year Published + Title
Average Rating + Title
The sorted list is saved back to the books.csv file

### Bubble Sort
Bubble sort is used to sort books within different bookshelves. This method sorts the list of dictionaries by two keys.


### Bucket Sort
Bucket sort is used to categorize books into different age groups (Children, Young Adult, Adult) and then sort each category by author and title.

## Greedy Algorithm

The greedy algorithm is used to calculate the maximum high-value books you can read within a certain time frame. This algorithm makes a locally optimal choice at each step by selecting the book with the highest value per hour that fits within the remaining available hours. This approach is efficient and provides a good approximation for maximizing the total value of books read within the given time frame.

## MST and Clustering

The MST (Minimum Spanning Tree) algorithm is used to cluster books by similarity. The algorithm calculates the similarity between books based on their genre and average rating, constructs an edge list, builds the MST using Kruskal's algorithm, and applies a greedy approach to form clusters by removing the highest-weight edges from the MST.


## How to Edit a Book
You can edit the following attributes of a book:

Read/Not Read & Date Read
Your Rating
Delete the book from the library
