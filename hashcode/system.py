from typing import List

from hashcode.library import Library
from hashcode.signup import SignUp


class System:

    def __init__(self, libraries: List[Library], books: List[int], n_days: int):
        self.libraries = list(sorted(libraries, key=lambda l: l.signup_days))
        self.books = books
        self.n_days = n_days

    def get_next_library(self, days_left: int, blacklist: List[int]):
        pass

    def generate_solution(self) -> List[SignUp]:
        
        days_left = self.n_days
        current_lib: Library = self.libraries.pop(0)
        result: [SignUp] = []
        books_scanned: [int] = []
        while current_lib is not None:
            books = current_lib.get_books_scanned_from_initialization_day(days_left, self.books)
            result.append(SignUp(current_lib.lib_id, books))
            for book in books:
                books_scanned.append(book)
            days_left -= current_lib.signup_days
            current_lib = self.get_next_library(days_left, books_scanned)
        return result
            

    # Should sort libraries by order of signup time increasing.
    # Then perform second pass and scan based on book scores, removing duplicates (or adding them to a blacklist).