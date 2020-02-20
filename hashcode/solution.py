# A fine thing indeed!
from typing import List

from hashcode.io import parse_data, write_submission
from hashcode.signup import SignUp
from hashcode.system import System

if __name__ == "__main__":
    n_books, n_libs, n_days, scores, libs = parse_data("a_example.txt")
    system = System(libraries=libs, books=scores, n_days=n_days)
    print(n_books)
    print(n_libs)
    print(libs)
    solution = system.generate_solution()
    write_submission(len(solution), solution)
