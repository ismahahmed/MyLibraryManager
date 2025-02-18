from helpers import Helpers
from tabulate import tabulate

class Sorting:
    def merge_sort(book_list, sorting_categories):
        if len(book_list) <= 1:
            return book_list
        
        left_half, right_half = Helpers.divide_books(book_list)

        sorted_left = Sorting.merge_sort(left_half, sorting_categories)
        sorted_right = Sorting.merge_sort(right_half, sorting_categories)

        return Sorting.merge(sorted_left, sorted_right, sorting_categories)

    def merge(left, right, sorting_categories):
        sorting_category1, sorting_category2 = sorting_categories[0], sorting_categories[1]
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][sorting_category1] < right[j][sorting_category1]:
                sorted_list.append(left[i])
                i += 1
            elif left[i][sorting_category1] > right[j][sorting_category1]:
                sorted_list.append(right[j])
                j += 1
            else:  
                if left[i][sorting_category2] < right[j][sorting_category2]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

    @staticmethod
    def bubble_sort_books(books, key1, key2):
        '''
        books: list of dictionaries
        Intent: Sort the list of dictionaries by key1 and key2
        PRECONDITION: books is a list of dictionaries, key1 and key2 are keys in the dictionaries
        POSTCONDITON: books and old(books) are identical in size
        POSTCONDITION: books is sorted
        returns books sorted
        '''
        n = len(books)
        for i in range(n):
            for j in range(0, n-i-1):
                if (books[j][key1], books[j][key2]) > (books[j+1][key1], books[j+1][key2]):
                    books[j], books[j+1] = books[j+1], books[j]
        return books

    @staticmethod
    def bucket_sort_books(library):
        '''
        library: dictionary of books
        Intent: sort the books in the library by age group
        PRECONDITION: library is not empty
        PRECONDITION: three age group options: children, young adult, adult
        POSTCONDITION: each book is in the correct age group
        POSTCONDITION: each age group is sorted by author_last_first and title
        returns buckets
        '''
        buckets = {
            'Children': [],
            'Young Adult': [],
            'Adult': []
        }

        for book in library:
            age_group = book['age_group']
            if age_group in buckets:
                buckets[age_group].append(book)

        for age_group in buckets:
            buckets[age_group] = Sorting.bubble_sort_books(buckets[age_group], 'author_last_first', 'title')

        return buckets

    @staticmethod
    def print_sorted_bookshelves(library):
        '''
        Prints the sorted bookshelves of a library.
        Args:
            library (dict): A dictionary representing the library with books categorized by age group.
        The function sorts the books using the bucket_sort_books method from the Sorting module
        and prints each category of books in a tabulated format.
        '''
        buckets = Sorting.bucket_sort_books(library)

        for age_group, books in buckets.items():
            print(f"\n{age_group} Bookshelf:")
            if not books:
                print("No books in this category.")
                continue

            headers = ["Title", "Author", "Year Published", "Average Rating", "Your Ratings", "Read", "Date Read"]
            books_display = [[
                book.get("title", "N/A"),
                book.get("author_first_last", "N/A"),
                book.get("year_published", "N/A"),
                book.get("avg_rating", "N/A"),
                book.get("my_rating", "N/A"),
                book.get("read", "N/A"),
                book.get("date_read", "N/A")
            ] for book in books]

            print(tabulate(books_display, headers=headers, tablefmt="pretty"))
