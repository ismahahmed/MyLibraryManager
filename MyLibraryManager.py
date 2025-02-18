import csv
import os
from tabulate import tabulate
from helpers import Helpers
from sorting import Sorting
from validation import Validation
from book import Book

CSV_FIELDS = [
    "title", "author_first_last", "author_last_first", "isbn", "isbn13",
    "my_rating", "avg_rating", "publisher", "binding", "num_pages",
    "year_published", "date_read", "genre", "age_group", "read"
]

class MyLibraryManager:
    def __init__(self, csv_file='data/books.csv'):
        self.library = Helpers.read_csv_as_dict(csv_file)
        self.csv_file = csv_file

    def view_books(self):
        """
        Displays all books stored in the CSV file in a formatted table
        
        Args:
            csv_file (str): Path to the CSV file containing book data
        """
        if self.library is None:
            print("Your library is empty. Please try adding a book!")
            return

        headers = ["Title", "Author", "Year Published", "Average Rating", "Your Ratings", "Read", "Date Read"]
        books_display = [[
            book.get("title", "N/A"),
            book.get("author_first_last", "N/A"),
            book.get("year_published", "N/A"),
            book.get("avg_rating", "N/A"),
            book.get("my_rating", "N/A"),
            book.get("read", "N/A"),
            book.get("date_read", "N/A")
        ] for book in self.library]

        print("\nYour Library:")
        print(tabulate(books_display, headers=headers, tablefmt="pretty"))
        print()

    def write_csv_header(self, writer):
        writer.writerow(CSV_FIELDS)

    def write_book_to_csv(self, writer, book):
        writer.writerow([
            book.title, book.author_first_last, book.author_last_first, book.isbn, book.isbn13,
            book.my_rating, book.avg_rating, book.publisher, book.binding, book.num_pages,
            book.year_published, book.date_read, book.genre, book.age_group, book.read
        ])

    def save_book_to_csv(self, book):
        """
        Saves the given Book object to a CSV file
        If the file does not exist, a header row is added
        
        Args:
            book (Book): The book object to be saved
            csv_file (str): Path to the CSV file where the book will be stored
        """
        file_exists = os.path.exists(self.csv_file)

        try:
            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)

                if not file_exists:
                    self.write_csv_header(writer)

                self.write_book_to_csv(writer, book)

            self.library = Helpers.read_csv_as_dict(self.csv_file)
        except Exception as e:
            print(f"Error saving book to CSV file: {e}")

    def add_book(self):
        """
        Gets user input to create book object
        Goes through input validation for: ISBN, ratings, binding type, number of pages, year, and age group
        
        Returns:
            Book: A Book object with user inputted details
        """
        print("Enter the following details for the book:")

        title = input("Title: ")
        author_first = input("Author's First Name: ")
        author_last = input("Author's Last Name: ")
        isbn = input("ISBN (leave blank if unknown): ")

        while isbn and not Validation.is_valid_isbn(isbn):
            print("Invalid ISBN. It should be exactly 10 characters long.")
            isbn = input("ISBN (leave blank if unknown): ")

        isbn13 = input("ISBN-13 (leave blank if unknown): ")
        while isbn13 and not Validation.is_valid_isbn13(isbn13):
            print("Invalid ISBN-13. It should be exactly 13 characters long.")
            isbn13 = input("ISBN-13 (leave blank if unknown): ")

        my_rating = input("Your Rating (leave blank if not rated): ") or None
        while my_rating and not Validation.is_valid_rating(my_rating):
            print("Invalid rating. It should be between 0 and 5.")
            my_rating = input("Your Rating (leave blank if not rated): ")
        my_rating = float(my_rating) if my_rating else None

        avg_rating = input("Average Rating on Goodreads: ")
        while avg_rating and not Validation.is_valid_rating(avg_rating):
            print("Invalid average rating. It should be between 0 and 5.")
            avg_rating = input("Average Rating on Goodreads: ")
        avg_rating = float(avg_rating) if avg_rating else None

        publisher = input("Publisher: ")
        binding = input("Binding (e.g., Paperback, Hardcover, eBook): ")
        while not Validation.is_valid_binding(binding):
            print("Invalid binding. It should be one of 'paperback', 'hardcover', or 'ebook'.")
            binding = input("Binding (e.g., Paperback, Hardcover, eBook): ")

        num_pages = input("Number of Pages: ")
        while not Validation.is_valid_num_pages(num_pages):
            print("Invalid number of pages. It should be a positive integer greater than 0.")
            num_pages = input("Number of Pages: ")

        year_published = input("Year Published: ")
        while not Validation.is_valid_year(year_published):
            print("Invalid year. It should be a 4-digit year (YYYY format).")
            year_published = input("Year Published: ")

        read = input("Have you read this book? (True/False): ").strip().lower() == "true"

        date_read = None
        if read:
            while True:
                date_read = input("Date you read the book (YYYY-MM-DD): ")
                if Validation.is_valid_date(date_read):
                    break
                else:
                    print("Invalid date format. Please use YYYY-MM-DD format.")
        else:
            date_read = ""

        genre = input("Genre: ")

        while True:
            age_group = input("Age Group (Children, Young Adult, Adult): ")
            if Validation.is_valid_age_group(age_group):
                break
            else:
                print("Invalid age group. Please enter 'Children', 'Young Adult', or 'Adult'.")
        age_group = age_group.title()

        book = Book(title, author_first, author_last, isbn, isbn13, my_rating, avg_rating,
                    publisher, binding, num_pages, year_published, date_read, genre, age_group, read)

        self.save_book_to_csv(book)

    def delete_library(self):
        """
        Deletes the entire book library (CSV file) upon user confirmation
        
        Args:
            csv_file (str): Path to the CSV file to be deleted
        """
        print("WARNING: This will permanently delete all books in your library")
        confirmation = input("Type 'delete library' to confirm or 'exit' to cancel: ").strip().lower()

        if confirmation == "delete library":
            try:
                os.remove(self.csv_file)
                print("Your library has been deleted.")
            except Exception as e:
                print(f"Error deleting library: {e}")
        else:
            print("Cancelled")

        self.library = Helpers.read_csv_as_dict(self.csv_file)

    def delete_book_from_csv(self, book):
        updated_books = []
        try:
            with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['title'].lower() != book.title.lower():
                        updated_books.append(row)

            Helpers.rewrite_csv(self.csv_file, updated_books)
            self.library = Helpers.read_csv_as_dict(self.csv_file)
        except Exception as e:
            print(f"Error deleting book from CSV file: {e}")

    def find_book_by_title(self, title):
        for index, book in enumerate(self.library):
            if book['title'].lower() == title.lower():
                return index, book
        return None, None

    def edit_book_details(self, book):
        book_details = [
            ["Title", book['title']],
            ["Author", book['author_first_last']],
            ["ISBN", book['isbn']],
            ["ISBN-13", book['isbn13']],
            ["My Rating", book['my_rating']],
            ["Average Rating", book['avg_rating']],
            ["Publisher", book['publisher']],
            ["Binding", book['binding']],
            ["Number of Pages", book['num_pages']],
            ["Year Published", book['year_published']],
            ["Date Read", book['date_read']],
            ["Genre", book['genre']],
            ["Age Group", book['age_group']],
            ["Read", "Yes" if book['read'] else "No"]
        ]

        print("\nFound book:")
        print(tabulate(book_details, tablefmt="pretty"))
        print()

        print("Choose what you want to edit:")
        print("1. Edit Read/Not Read & Date Read")
        print("2. Edit Rating")
        print("3. Delete this book")
        print("4. Cancel")

        choice = input("Select an option (1/2/3/4): ").strip()

        if choice == "1":
            new_read = input("Have you read this book? (True/False): ").strip().lower() == "true"
            if new_read:
                date_read = input("Enter the new date you read the book (YYYY-MM-DD): ")
                while not Validation.is_valid_date(date_read):
                    date_read = input("Invalid date. Please use YYYY-MM-DD format: ")
            else:
                date_read = ""
            book['read'] = new_read
            book['date_read'] = date_read

        elif choice == "2":
            new_rating = input("Enter your new rating (0-5): ")
            while not Validation.is_valid_rating(new_rating):
                new_rating = input("Invalid rating. Please enter a number between 0 and 5: ")
            book['my_rating'] = new_rating

        elif choice == "3":
            confirm = input(f"Are you sure you want to delete '{book['title']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                return "delete"

        elif choice == "4":
            print("No changes made.")
            return "cancel"

        return "edit"

    def update_csv_file(self):
        Helpers.rewrite_csv(self.csv_file, self.library)
        self.library = Helpers.read_csv_as_dict(self.csv_file)

    def edit_book(self):
        edit_title = input("Enter book title you would like to edit: ")
        index, book = self.find_book_by_title(edit_title)

        if book is None:
            print(f"Book titled '{edit_title}' not found in the library.\n")
            return

        action = self.edit_book_details(book)

        if action == "delete":
            self.library.pop(index)
            print(f"'{book['title']}' has been deleted from your library.")
        elif action == "edit":
            print(f"Changes to '{book['title']}' have been saved.\n")

        self.update_csv_file()

    def make_sorting_choice(self):
        print("This option allows you to sort and save your CSV file how you want your books sorted")
        print("Sort by categories: ")
        print("1: By Author Last Name, First Name + Title")
        print("2: Year Published + Title")
        print("3: Average Rating + Title")
        sort_choice = input("Please select how you would like to sort: (1, 2, 3): ")
        if sort_choice == "1":
            sorting_by = ['author_last_first', 'title']
        elif sort_choice == "2":
            sorting_by = ['year_published', 'title']
        elif sort_choice == "3":
            sorting_by = ['avg_rating', 'title']
        else:
            sorting_by = "Fail"
            print("\nInvalid choice. Please try again.")
        return sorting_by
    
    def get_optimized_time(self, book, pages_per_hour, memo):
        """
        PRECONDITION: book is a dictionary containing book details, pages_per_hour is a float, memo is a dictionary
        RETURNS: hours_for_book
        POST1: hours_for_book is the time required to read the book
        POST2: memo is updated with the calculated time for the book

        Args:
            book (dict): A dictionary containing book details
            pages_per_hour (float): The reading speed in pages per hour
            memo (dict): A dictionary to store the calculated time for each book

        Returns:
            float: The time required to read the book
        """
        book_id = (book.get('title'), book.get('author_first_last'))  # Using title and author as a unique identifier
        if book_id in memo:
            return memo[book_id]
        
        num_pages = int(book.get('num_pages', 0))
        hours_for_book = num_pages / pages_per_hour
        memo[book_id] = hours_for_book
        return hours_for_book

    def get_total_hours(self, books, pages_per_hour):
        """
        PRECONDITION: books is a list of dictionaries containing book details, pages_per_hour is a float
        RETURNS: total_hours
        POST1: total_hours is the total time required to read all books in the list
        POST2: memo is updated with the calculated time for each book

        Args:
            books (list): A list of dictionaries containing book details
            pages_per_hour (float): The reading speed in pages per hour

        Returns:
            float: The total time required to read all books in the list
        """
        total_hours = 0
        memo = {}
        for book in books:
            total_hours += self.get_optimized_time(book, pages_per_hour, memo)
        return total_hours

    def estimate_reading_time(self, pages_per_hour):
        """
        PRECONDITION: pages_per_hour is a float
        RETURNS: None
        POST1: Prints the estimated time to read all unread books in the library

        Args:
            pages_per_hour (float): The reading speed in pages per hour
        """
        unread_books = [book for book in self.library if not book.get('read', 'False').lower() == 'true']
        total_hours = self.get_total_hours(unread_books, pages_per_hour)
        print(f"Estimated time to read all unread books: {total_hours:.2f} hours")



    def menu(self):
        while True:
            print("\n--- Library Manager ---")
            print("1. View Books")
            print("2. Add a Book")
            print("3. Edit Book")
            print("4. Sort Books")
            print("5. Print Sorted Bookshelves")
            print("6. Delete Library")
            print("7. Estimate Total Reading Time for Unread Books")
            print("8. Exit")
            print("-----------------------\n")
            choice = input("Select an option (1/2/3/4/5/6/7): ").strip()

            if choice == "1":
                self.view_books()

            elif choice == "2":
                self.add_book()
                self.library = Helpers.read_csv_as_dict(self.csv_file)
            elif choice == "3":
                self.edit_book()
                self.library = Helpers.read_csv_as_dict(self.csv_file)

            elif choice == "4":
                sorting_by = self.make_sorting_choice()
                while sorting_by == "Fail":
                    sorting_by = self.make_sorting_choice()

                books = Helpers.read_csv_as_dict(self.csv_file)
                sorted_books = Sorting.merge_sort(books, sorting_by)
                Helpers.rewrite_csv(self.csv_file, sorted_books)
                self.library = Helpers.read_csv_as_dict(self.csv_file)

            elif choice == "5":
                Sorting.print_sorted_bookshelves(self.library)

            elif choice == "6":
                self.delete_library()
                self.library = Helpers.read_csv_as_dict(self.csv_file)

            elif choice == "7":
                pages_per_hour = float(input("Enter your reading speed (pages per hour): "))
                self.estimate_reading_time(pages_per_hour)

            elif choice == "8":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

def main():
    m = MyLibraryManager()
    m.menu()

if __name__ == "__main__":
    main()