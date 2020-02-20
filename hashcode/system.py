from typing import List

from hashcode.library import Library


class System:

    def __init__(self, libraries: List[Library], books: List[int]):
        self.libraries = libraries
        self.books = books

    def generate_solution(self):
        sorted_libs = sorted(self.libraries, key=lambda l: l.signup_days)

    # Should sort libraries by order of signup time increasing.
    # Then perform second pass and scan based on book scores, removing duplicates (or adding them to a blacklist).