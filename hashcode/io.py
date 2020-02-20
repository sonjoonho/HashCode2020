from typing import List

from hashcode.library import Library
from hashcode.signup import SignUp


def parse_data(filename: str):
    with open(f"../data/{filename}") as f:
        data = f.readlines()
        line_one = data[0].split(' ')
        n_books = int(line_one[0])
        n_libs = int(line_one[1])
        n_days = int(line_one[2])
        scores = [int(s) for s in data[1].split(' ')]

        data = data[2:]

        libs = []
        for i in range(0, (n_libs * 2), 2):
            id = i // 2
            lib_data = data[i].split(' ')
            n_lib_books = int(lib_data[0])
            signup_days = int(lib_data[1])
            scan_limit = int(lib_data[2])
            lib_books = [int(b) for b in data[i + 1].split(' ')]

            libs.append(Library(id, n_lib_books, lib_books, signup_days, scan_limit))
        assert n_libs == len(libs)
        return n_books, n_libs, n_days, scores, libs


"""
Expecting a list of tuples/objects that have the fields

id: id of the library
k: number of books to scan from the library
book_ids: the ids of the books to scan from that library in the order in which they are scanned without duplicates
"""


def write_submission(n_libs: int, solutions: List[SignUp], filename="solution.txt"):
    lines = [str(n_libs)]
    for s in solutions:
        lines.append(f"{s.lib_id} {s.n_books}")
        lines.append(f"{' '.join(str(s) for s in s.book_ids)}")
    with open(filename, "wt") as f:
        f.writelines('\n'.join(lines))
