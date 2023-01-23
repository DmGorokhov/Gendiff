#!/usr/bin/env python3


import gendiff.cli as cli
import gendiff.comparator as comparator


def main():
    filepath_1, filepath_2 = cli.get_files()
    result = comparator.generate_diff(filepath_1, filepath_2)
    print(result)


if __name__ == '__main__':
    main()
