import json

from gendiff.formatters.diff2json import get_json
from gendiff.diff_units.data_comparator import get_diff
from gendiff.diff_units.data_parser import read_file


data1 = read_file('tests/fixtures/file1.json')
data2 = read_file('tests/fixtures/file2.json')
data1_nested = read_file('tests/fixtures/file1_nested.json')
data2_nested = read_file('tests/fixtures/file2_nested.json')


expected_json_plain = read_file('tests/fixtures/plain_diff.json')
expected_json_nested = read_file('tests/fixtures/nested_diff.json')


def test_get_json():
    diff_plain = get_diff(data1, data2)
    diff_nested = get_diff(data1_nested, data2_nested)
    json_diff_plain = json.loads(get_json(diff_plain))
    json_diff_nested = json.loads(get_json(diff_nested))

    assert json_diff_plain == expected_json_plain
    assert json_diff_nested == expected_json_nested
