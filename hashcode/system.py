from typing import List, Optional, Set

from hashcode.library import Library
from hashcode.signup import SignUp


class System:

    def __init__(self, libraries: List[Library], books: List[int], n_days: int):
        self.libraries = list(sorted(libraries, key=lambda l: l.signup_days))
        for lib in self.libraries:
            lib.sort_books(scores=books)
        self.books = books
        self.n_days = n_days

    def generate_solution(self) -> List[SignUp]:
        
        days_left = self.n_days
        books_scanned: Set[int] = set()
        current_lib: Library = self.get_next_lib(days_left, books_scanned)
        result: [SignUp] = []
        while current_lib is not None:
            books = current_lib.get_books_scanned_from_signup_day(days_left)
            result.append(SignUp(current_lib.lib_id, books))
            for book in books:
                books_scanned.add(book)
            days_left -= current_lib.signup_days
            current_lib = self.get_next_lib(days_left, books_scanned)
        return result
            

    def get_next_lib(self, days_left: int, blacklist: Set[int]) -> Optional[Library]:

        # 1. No libs left
        # 2. No days left
        best_lib = None
        best_score = 0

        for lib in self.libraries:
            if lib.signup_days > days_left:
                break
            score = self._compute_score_and_remove_blacklisted_books(lib, days_left, blacklist)
            if score > best_score:
                best_lib = lib
                best_score = score

        # No further valid candidate libraries
        return best_lib

    def _compute_score_and_remove_blacklisted_books(self, library: Library, days_left: int, blacklist: Set[int]) -> int:
        """
        Checks that the library has book that are not in the blacklist.
        WARNING: This function removes books that are in the blaclist from the library -> side effecting!
        """

        non_blacklist_books = []
        while library.books:
            book = library.books.pop(0)
            if book not in blacklist:
                non_blacklist_books.append(book)

        library.books = non_blacklist_books

        return library.get_score_for_signup_day(days_left, self.books)

    # Should sort libraries by order of signup time increasing.
    # Then perform second pass and scan based on book scores, removing duplicates (or adding them to a blacklist).