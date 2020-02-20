from typing import List

from hashcode.library import Library


class System:

    def __init__(self, libraries: List[Library], books: List[int]):
        self.libraries = libraries
        self.books = books

    def generate_solution(self):
        sorted_libs = sorted(self.libraries, key=lambda l: l.signup_days)

    def get_next_lib(self, days_left: int, blacklist: List[int]):
        # 1. No libs left
        # 2. No days left

        # Need to blacklist
        while self.libraries:
            lib = self.libraries.pop()
            if self._library_is_valid(lib, days_left, blacklist):
                return lib

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