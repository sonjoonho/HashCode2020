# A fine thing indeed!
from typing import List

from hashcode.io import parse_data

if __name__ == "__main__":
    n_books, n_libs, n_days, scores, libs = parse_data("f_libraries_of_the_world.txt")
    print(n_books)
    print(n_libs)
    print(libs)