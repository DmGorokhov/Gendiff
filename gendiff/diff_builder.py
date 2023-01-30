from gendiff.comparator.diff_counter import get_diff, console_output
from gendiff.comparator.data_parser import read_file


def generate_diff(filepath_old, filepath_new):
    old_data = read_file(filepath_old)
    new_data = read_file(filepath_new)

    compare_result = get_diff(old_data, new_data)
    diff_report = console_output(old_data, new_data, compare_result)

    return diff_report
