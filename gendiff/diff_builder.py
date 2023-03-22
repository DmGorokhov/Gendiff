from gendiff.diff_units.data_comparator import get_diff
from gendiff.diff_units.data_parser import read_file
import gendiff.diff_units.stylish as stylish


def generate_diff(filepath_old, filepath_new, format='stylish'):
    old_data = read_file(filepath_old)
    new_data = read_file(filepath_new)

    diff = get_diff(old_data, new_data)
    if format == 'stylish':
        diff_report = stylish.get_stylish(diff)
    return diff_report
