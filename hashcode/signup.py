from typing import List


class SignUp:

    def __init__(self, library_id: int, book_ids: List[int]):
        self.lib_id = library_id
        self.book_ids = book_ids
        self.n_books = len(self.book_ids)
