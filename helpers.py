import csv
import os

class Helpers:
    @staticmethod
    def read_csv_as_dict(csv_file):
        if not os.path.exists(csv_file):
            print(f"File {csv_file} does not exist.")
            return []

        books = []
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(row)
        
        return books


    @staticmethod
    def divide_books(book_list):
        '''
        book_list: list of dictionaries
        INTENT: Divide book_list into a 2 parts
        EXAMPLE: [{'title': 'Six of Crows (Six of Crows, #1)',...}, {'title': 'The Awakening', 'author_first_last': 'Kate Chopin',...}]
        RETURNS 2 list of even sized (or about even sized) dictionaries):
        [{'title': 'Six of Crows (Six of Crows, #1)',...}], [{'title': 'The Awakening', 'author_first_last': 'Kate Chopin',...}],
        RETURNS book_list[:mid], book_list[mid:]

        POSTCONDITION 1 (Parts Sufficient):  
        Knowing DesiredIORelationship(return_subspaces[i], return_solution[i]) for every i facilitates the 
        implementation of DesiredIORelationship(book_list, return_solution)

        POSTCONDITION 2 (Parts Homogeneous):  The elements of return_subspaces are lists containing the same type of objects as book_list 
        POSTCONDITION 3 (Count Fixed):  The number of elements in return_subspaces is independent of book_list
        POSTCONDITION 4 (Proportions Comparable):  In size, the elements in return_subspaces are all comparable 
        fractions of the size of book_list. For example, if divided into halves, the parts are approximately equal in size.
        '''
        mid = len(book_list) // 2
        return book_list[:mid], book_list[mid:]

    @staticmethod
    def rewrite_csv(csv_file, books):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = books[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)