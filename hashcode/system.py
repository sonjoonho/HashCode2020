from typing import List, Optional, Set, Tuple

from hashcode.library import Library
from hashcode.signup import SignUp


class System:

    def __init__(self, libraries: List[Library], books: List[int], n_days: int):
        self.libraries = list(sorted(libraries, key=lambda l: l.signup_days))
        self.books = books
        self.n_days = n_days

    def generate_solution(self, window_size) -> Tuple[List[SignUp], int]:

        days_left = self.n_days
        total_score = 0
        books_scanned: Set[int] = set()
        current_lib: Library = self.get_next_lib(days_left, books_scanned, window_size)
        result: [SignUp] = []
        while current_lib is not None:
            books = current_lib.get_books_scanned_from_initialization_day(days_left, self.books)
            result.append(SignUp(current_lib.lib_id, books))
            for book in books:
                books_scanned.add(book)
                total_score += self.books[book]
            days_left -= current_lib.signup_days
            current_lib = self.get_next_lib(days_left, books_scanned, window_size)
        return result, total_score

    def get_next_lib(self, days_left: int, blacklist: Set[int], window_size: int) -> Optional[Library]:

        # 1. No libs left
        # 2. No days left
        best_lib = None
        best_score = 0
        current_index = 0
        while current_index < window_size and current_index < len(self.libraries):
            lib = self.libraries[current_index]
            if not self._library_is_valid(lib, days_left, blacklist):
                self.libraries.pop(current_index)
                continue
            books = lib.get_books_scanned_from_initialization_day(days_left, self.books)
            score = sum([self.books[book] for book in books])
            if score > best_score:
                best_lib = lib
                best_score = score
            current_index += 1

        # No further valid candidate libraries
        if best_lib is not None:
            self.libraries.remove(best_lib)
        return best_lib

    def _library_is_valid(self, library: Library, days_left: int, blacklist: Set[int]) -> bool:
        """
        Checks that the library has book that are not in the blacklist.
        WARNING: This function removes books that are in the blaclist from the library -> side effecting!
        """
        if library.signup_days > days_left:
            return False

        non_blacklist_books = []
        while library.books:
            book = library.books.pop(0)
            if book not in blacklist:
                non_blacklist_books.append(book)

        library.books = non_blacklist_books

        return len(non_blacklist_books) > 0

    # Should sort libraries by order of signup time increasing.
    # Then perform second pass and scan based on book scores, removing duplicates (or adding them to a blacklist).
