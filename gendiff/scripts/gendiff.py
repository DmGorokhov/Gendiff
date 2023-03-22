#!/usr/bin/env python3


import gendiff.cli as cli
from gendiff.diff_builder import generate_diff


def main():
    filepath_1, filepath_2, format = cli.get_files()
    diff_result = generate_diff(filepath_1, filepath_2, format)
    print(diff_result)


if __name__ == '__main__':
    main()
