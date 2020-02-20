class System:

    def __init__(self, libraries):
        self.libraries = libraries
        self.sorted_libs = sorted(libraries, key=lambda l: l.signup_days)

    # Should sort libraries by order of signup time increasing.
    # Then perform second pass and scan based on book scores, removing duplicates (or adding them to a blacklist).