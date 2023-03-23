from gendiff.diff_units.plain import get_plain, to_plain_val
from gendiff.diff_units.data_comparator import get_diff
from gendiff.diff_units.data_parser import read_file



data1_nested = read_file('tests/fixtures/file1_nested.yaml')
data2_nested = read_file('tests/fixtures/file2_nested.yaml')

def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_to_plain_val():
    assert to_plain_val(False) == 'false'
    assert to_plain_val(True) == 'true'
    assert to_plain_val(None) == 'null'
    assert to_plain_val('') == "''"
    assert to_plain_val('Hello!') == "'Hello!'"
    assert to_plain_val(7) == "'7'"
    assert to_plain_val(0) == "'0'"
    assert to_plain_val({'a': 1, 'b': 1, 'c': 3}) == '[complex value]'


def test_get_plain():
    expected_output = read('tests/fixtures/plain_output.txt')
    diff = get_diff(data1_nested, data2_nested)
    
    assert get_plain(diff) == expected_output
     