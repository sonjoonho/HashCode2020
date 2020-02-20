from typing import List


class Library:

    def __init__(self, books: List[int], signup_days: int, scan_limit: int):
        self.books = books
        self.signup_days = signup_days
        self.scan_limit = scan_limit
