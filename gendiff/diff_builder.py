from gendiff.diff_units.data_comparator import get_diff
from gendiff.diff_units.data_parser import read_file
from gendiff.diff_units.stylish import get_stylish
from gendiff.diff_units.plain import get_plain
from gendiff.diff_units.diff2json import get_json


def generate_diff(filepath_old, filepath_new, format='stylish'):
    old_data = read_file(filepath_old)
    new_data = read_file(filepath_new)

    diff = get_diff(old_data, new_data)
    match format:
        case 'stylish':
            diff_report = get_stylish(diff)
        case 'plain':
            diff_report = get_plain(diff)
        case 'json':
            diff_report = get_json(diff)
    return diff_report
