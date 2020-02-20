# A fine thing indeed!
from typing import List

from hashcode.parse import parse_data

if __name__ == "__main__":
    n_books, n_libs, n_days, scores, libs = parse_data("b_read_on.txt")
    print(n_books)
    print(n_libs)
    print(libs)