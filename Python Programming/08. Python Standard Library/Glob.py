"""
File Wildcards
The glob module provides a function for making file lists from directory wildcard searches:
"""
import os
import glob
from pathlib import Path


def test_glob():
    """File Wildcards."""
    # == operator for lists relies on the order of elements in the list.
    # In some cases the glob() function returns list
    # in reverse order then  it might be expected. Thus lets sort both lists before comparison
    # using sorted() built-in function.
    assert sorted(glob.glob("glob_files\\*.txt")) == sorted(
        ["glob_files\\first_file.txt", "glob_files\\second_file.txt"]
    )


test_glob()
