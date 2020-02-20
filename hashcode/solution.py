# A fine thing indeed!
from typing import List

from hashcode.io import parse_data, write_submission
from hashcode.system import System

if __name__ == "__main__":
    filenames = ["a_example.txt",
                 "b_read_on.txt",
                 "c_incunabula.txt",
                 "d_tough_choices.txt",
                 "e_so_many_books.txt",
                 "f_libraries_of_the_world.txt"
                 ]
    for filename in filenames:
        print(filename, ", chance would be a fine thing")
        best_solution = None
        best_score = 0
        best_window = 0
        windows = [10, 100, 500, 1000]
        for window in windows:
            n_books, n_libs, n_days, scores, libs = parse_data(filename)
            system = System(libraries=libs, books=scores, n_days=n_days)
            solution, total_score = system.generate_solution(window)
            if total_score > best_score:
                best_solution = solution
                best_score = total_score
                best_window = window
        write_submission(len(best_solution), best_solution, filename=f"{filename}_solution.txt")
        print("A fine thing indeed")
        print(best_window)

