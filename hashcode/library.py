from typing import List


class Library:

    def __init__(self, lib_id, n_books, books: List[int], signup_days: int, scan_limit: int):
        self.lib_id = lib_id
        self.n_books = n_books
        self.books = books
        self.signup_days = signup_days
        self.scan_limit = scan_limit

    def __repr__(self):
        return f"Library(id={self.lib_id})"

    """Uses the days left (assuming signup has not started yet) and
    returns a list of tuples of exact books to return.
    """

    def get_books_scanned_from_initialization_day(self, days_left: int, scores: List[int]):
        # Sort books in score descending

        # Get scores of books
        sorted_books = list(sorted(self.books, key=lambda b: scores[b]))

        days_left -= self.signup_days
        books_scanned = []
        while days_left > 0 and sorted_books:
            for _ in range(self.scan_limit):
                if not sorted_books:
                    break
                books_scanned.append(sorted_books.pop(0))
            days_left -= 1

        return books_scanned
