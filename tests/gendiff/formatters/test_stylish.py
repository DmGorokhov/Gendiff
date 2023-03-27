from gendiff.formatters.stylish import to_stylish_val, get_stylish
from gendiff.diff_units.data_comparator import get_diff
from gendiff.diff_units.data_parser import read_file

nested_val = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}

data1_plain = read_file('tests/fixtures/file1.json')
data2_plain = read_file('tests/fixtures/file2.json')
data1_nested = read_file('tests/fixtures/file1_nested.yaml')
data2_nested = read_file('tests/fixtures/file2_nested.yaml')


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_to_stylish_val_primirives():
    assert to_stylish_val(False) == 'false'
    assert to_stylish_val(True) == 'true'
    assert to_stylish_val(None) == 'null'
    assert to_stylish_val('') == ''
    assert to_stylish_val('How are you?') == 'How are you?'
    assert to_stylish_val(7) == '7'


def test_to_stylish_val_nested():
    expected_str = read('tests/fixtures/stringify_nested_output.txt')
    assert to_stylish_val(nested_val) == expected_str


def test_get_stylish():
    expected_plain_output = read('tests/fixtures/stylish_plain_output.txt')
    expected_nested_output = read('tests/fixtures/stylish_nested_output.txt')
    plain_diff = get_diff(data1_plain, data2_plain)
    nested_diff = get_diff(data1_nested, data2_nested)

    assert get_stylish(plain_diff) == expected_plain_output
    assert get_stylish(nested_diff) == expected_nested_output
