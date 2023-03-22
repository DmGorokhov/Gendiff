import json
from yaml import safe_load

from gendiff.diff_units.data_comparator import get_diff
from gendiff.diff_units.data_parser import read_file


data1_json = read_file('tests/fixtures/file1.json')
data2_json = read_file('tests/fixtures/file2.json')
data1_json_nested = read_file('tests/fixtures/file1_nested.json')
data2_json_nested = read_file('tests/fixtures/file2_nested.json')
data1_yaml = read_file('tests/fixtures/file1.yaml')
data2_yaml = read_file('tests/fixtures/file2.yaml')
data1_yaml_nested = read_file('tests/fixtures/file1_nested.yaml')
data2_yaml_nested = read_file('tests/fixtures/file2_nested.yaml')


expected_diff = {'follow': {'status': 'deleted', 'value': False}, 
                 'host': {'status': 'unchanged', 'value': 'hexlet.io'},
                 'verbose': {'status': 'added', 'value': True}, 
                 'timeout': {'status': 'changed', 'old_value': 50, 'value': 20}, 
                 'proxy': {'status': 'deleted', 'value': '123.234.53.22'}}

not_changed = {'follow': {'status': 'unchanged', 'value': False}, 
               'host': {'status': 'unchanged', 'value': 'hexlet.io'},
               'timeout': {'status': 'unchanged', 'value': 50}, 
               'proxy': {'status': 'unchanged', 'value': '123.234.53.22'}}
expected_diff_nested = read_file('tests/fixtures/nested_diff.json')


def test_get_diff():
    diff_plain_json = get_diff(data1_json, data2_json)
    diff_plain_yaml = get_diff(data1_yaml, data2_yaml)
    nothing_changed_json = get_diff(data1_json, data1_json)
    nothing_changed_yaml = get_diff(data1_yaml, data1_yaml)
    diff_nested_json = get_diff(data1_json_nested, data2_json_nested)
    diff_nested_yaml = get_diff(data1_yaml_nested, data2_yaml_nested)

    assert diff_plain_json == expected_diff
    assert diff_plain_yaml == expected_diff
    assert nothing_changed_json == not_changed
    assert nothing_changed_yaml == not_changed
    assert diff_nested_json == expected_diff_nested
    assert diff_nested_yaml == expected_diff_nested
