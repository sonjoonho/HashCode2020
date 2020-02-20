# A fine thing indeed!
from typing import List

from hashcode.io import parse_data, write_submission
from hashcode.system import System

if __name__ == "__main__":
    filename = "e_so_many_books.txt"
    n_books, n_libs, n_days, scores, libs = parse_data(filename)
    system = System(libraries=libs, books=scores, n_days=n_days)
    solution = system.generate_solution()
    write_submission(len(solution), solution, filename=f"{filename}_solution.txt")
