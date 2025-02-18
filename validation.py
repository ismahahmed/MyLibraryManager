from datetime import datetime

class Validation:
    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_rating(rating):
        try:
            rating = float(rating)
            return 0 <= rating <= 5
        except ValueError:
            return False

    @staticmethod
    def is_valid_age_group(age_group):
        valid_groups = ['children', 'young adult', 'adult']
        return age_group.lower() in valid_groups

    @staticmethod
    def is_valid_num_pages(num_pages):
        try:
            num_pages = int(num_pages)
            return num_pages > 0
        except ValueError:
            return False

    @staticmethod
    def is_valid_year(year):
        try:
            year = int(year)
            return 1000 <= year <= 9999
        except ValueError:
            return False

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 10

    @staticmethod
    def is_valid_isbn13(isbn13):
        return len(isbn13) == 13

    @staticmethod
    def is_valid_binding(binding):
        valid_bindings = ['paperback', 'hardcover', 'ebook']
        return binding.lower() in valid_bindings