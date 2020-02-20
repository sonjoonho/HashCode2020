from typing import List, Optional

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
        books_scanned: [int] = []
        current_lib: Library = self.get_next_library(days_left, books_scanned)
        result: [SignUp] = []
        while current_lib is not None:
            books = current_lib.get_books_scanned_from_initialization_day(days_left, self.books)
            result.append(SignUp(current_lib.lib_id, books))
            for book in books:
                books_scanned.append(book)
            days_left -= current_lib.signup_days
            current_lib = self.get_next_library(days_left, books_scanned)
        return result
            

    def get_next_lib(self, days_left: int, blacklist: List[int]) -> Optional[Library]:

        # 1. No libs left
        # 2. No days left

        while self.libraries:
            lib = self.libraries.pop()
            if self._library_is_valid(lib, days_left, blacklist):
                return lib

        # No further valid candidate libraries
        return None

    def _library_is_valid(self, library: Library, days_left: int, blacklist: List[int]) -> bool:
        """
        Checks that the library has book that are not in the blacklist.
        WARNING: This function removes books that are in the blaclist from the library -> side effecting!
        """
        if library.signup_days > days_left:
            return False

        non_blacklist_books = []
        while library.books:
            book = library.books.pop()
            if book not in blacklist:
                non_blacklist_books.append(book)

        library.books = non_blacklist_books

        return len(non_blacklist_books) > 0

    # Should sort libraries by order of signup time increasing.
    # Then perform second pass and scan based on book scores, removing duplicates (or adding them to a blacklist).