#!/usr/bin/env python3


import gendiff.cli as cli
import gendiff.diff_builder as diff_builder


def main():
    filepath_1, filepath_2 = cli.get_files()
    diff_result = diff_builder.generate_diff(filepath_1, filepath_2)
    print(diff_result)


if __name__ == '__main__':
    main()
