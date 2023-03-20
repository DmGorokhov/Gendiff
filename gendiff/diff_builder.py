from gendiff.comparator.diff_counter import get_diff
from gendiff.comparator.data_parser import read_file
import gendiff.comparator.stylish as stylish


def generate_diff(filepath_old, filepath_new):
    old_data = read_file(filepath_old)
    new_data = read_file(filepath_new)

    diff = get_diff(old_data, new_data)
    diff_report = stylish.get_stylish(diff)
    return diff_report
