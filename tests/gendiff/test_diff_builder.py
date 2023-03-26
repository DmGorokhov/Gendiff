from gendiff.diff_builder import generate_diff
from gendiff.diff_units.data_parser import read_file
import json

filepath_old_plain = 'tests/fixtures/file1.json'
filepath_new_plain = 'tests/fixtures/file2.json'
filepath_old_nested = 'tests/fixtures/file1_nested.json'
filepath_new_nested = 'tests/fixtures/file2_nested.json'


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

expected_stylish_plain = read('tests/fixtures/stylish_plain_output.txt')
expected_stylish_nested = read('tests/fixtures/stylish_nested_output.txt')
expected_plain_output = read('tests/fixtures/plain_output.txt')
expected_json_plain = read_file('tests/fixtures/plain_diff.json')
expected_json_nested = read_file('tests/fixtures/nested_diff.json')



def test_generate_diff():
    diff_default_plain = generate_diff(filepath_old_plain, filepath_new_plain)
    diff_default_nested = generate_diff(filepath_old_nested, filepath_new_nested)
    
    assert diff_default_plain == expected_stylish_plain
    assert diff_default_nested == expected_stylish_nested

    diff_stylish_plain = generate_diff(filepath_old_plain, filepath_new_plain, 'stylish')
    diff_stylish_nested = generate_diff(filepath_old_nested, filepath_new_nested, 'stylish')

    assert diff_stylish_plain == expected_stylish_plain
    assert diff_stylish_nested == expected_stylish_nested
    
    diff_plain = generate_diff(filepath_old_nested, filepath_new_nested, 'plain')

    assert diff_plain == expected_plain_output

    diff_json_plain = json.loads(generate_diff(filepath_old_plain, filepath_new_plain, 'json'))
    diff_json_nested = json.loads(generate_diff(filepath_old_nested, filepath_new_nested, 'json'))

    assert diff_json_plain == expected_json_plain
    assert diff_json_nested == expected_json_nested
