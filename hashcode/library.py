from typing import List


class Library:

    def __init__(self, id, n_books, books: List[int], signup_days: int, scan_limit: int):
        self.id = id
        self.n_books = n_books
        self.books = books
        self.signup_days = signup_days
        self.scan_limit = scan_limit

    def __repr__(self):
        return f"Library(id={self.id})"

