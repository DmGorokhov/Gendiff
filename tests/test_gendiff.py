import pytest
import json
from yaml import safe_load
import tests.fixtures.py_fixtures as py_fixtures


from gendiff.cli import parse_args
from gendiff.diff_units.data_parser import read_file
from gendiff.diff_units.data_comparator import (get_diff, get_key_name,
                                                get_children, get_value,
                                                get_old_value, get_status,
                                                is_changed_key
                                                )
from gendiff.formatters.stylish import get_stylish, to_stylish_val
from gendiff.formatters.plain import get_plain, to_plain_val
from gendiff.formatters.json import get_json
from gendiff.diff_builder import generate_diff

fixtures_path = 'tests/fixtures/'
no_changes_case = py_fixtures.NOT_CHANGED
expected_diff_plain = py_fixtures.EXPECTED_DIFF
expected_diff_nested = py_fixtures.EXPECTED_DIFF_NESTED


def get_fixture_path(file_name):
    return fixtures_path + file_name


def read_fixture(fixture_name):
    with open(get_fixture_path(fixture_name), 'r') as f:
        data = f.read()
    return data


def read_json(filename):
    with open(get_fixture_path(filename), 'r') as f:
        data = json.load(f)
    return data


def read_yaml(filename):
    with open(get_fixture_path(filename), 'r') as f:
        data = safe_load(f)
    return data


def test_parse_args():
    args1 = parse_args(['file1', 'file2', '--format', 'plain'])
    args2 = parse_args(['file3', 'file4'])

    assert args1 == ('file1', 'file2', 'plain')
    assert args2 == ('file3', 'file4', 'stylish')


data_pasred_cases = [
    ('file1.json', read_json('file1.json')),
    ('file1.yml', read_yaml('file1.yml')),
    ('file2.json', read_json('file2.json')),
    ('file2.yml', read_yaml('file2.yml')),
    ('file1_nested.json', read_json('file1_nested.json')),
    ('file1_nested.yaml', read_yaml('file1_nested.yaml')),
    ('file2_nested.json', read_json('file2_nested.json')),
    ('file2_nested.yaml', read_yaml('file2_nested.yaml')),
]


@pytest.mark.parametrize('filename , load_result', data_pasred_cases)
def test_read_file(filename, load_result):
    assert read_file(get_fixture_path(filename)) == load_result


def test_read_file_wrong_format():
    with pytest.raises(Exception) as exeption:
        read_file(get_fixture_path('file1.txt'))
    assert str(exeption.value) == 'Files should be json or yaml format'


diff_cases = [(read_json('file1.json'), read_json('file2.json'),
               expected_diff_plain),
              (read_yaml('file1.yml'), read_yaml('file2.yml'),
               expected_diff_plain),
              (read_json('file1.json'), read_json('file1.json'),
               no_changes_case),
              (read_yaml('file1.yml'), read_yaml('file1.yml'),
               no_changes_case),
              (read_json('file1_nested.json'), read_json('file2_nested.json'),
               expected_diff_nested),
              (read_yaml('file1_nested.yaml'), read_yaml('file2_nested.yaml'),
               expected_diff_nested)
              ]


@pytest.mark.parametrize('data_1, data_2, diff', diff_cases)
def test_get_diff(data_1, data_2, diff):
    assert get_diff(data_1, data_2) == diff


key_diff = ('group1', ['unchanged', None, None, 'we are children'])
key_diff2 = ('group2', ['unchanged', None, 2023, None])
key_diff3 = ('group3', ['updated', 'young', 'old', None])
key_diff4 = ('group4', ['removed', False, None, None])
key_diff5 = ('group5', ['added', None, 0, None])
key_diff6 = ('group6', ['unchanged', None, {'a': 2, 'g': 'gh'}, None])


key_diffs = [(key_diff,
             'group1', 'unchanged', None, None, 'we are children', True),
             (key_diff2, 'group2', 'unchanged', None, 2023, None, False),
             (key_diff3, 'group3', 'updated', 'young', 'old', None, True),
             (key_diff4, 'group4', 'removed', False, False, None, True),
             (key_diff5, 'group5', 'added', None, 0, None, True),
             (key_diff6,
             'group6', 'unchanged', None, {'a': 2, 'g': 'gh'}, None, False)
             ]


@pytest.fixture(params=key_diffs)
def get_key_diffs(request):
    return request.param


def test_key_diff(get_key_diffs):
    key_diff, name, status, ola_value, value, children, changed = get_key_diffs
    assert get_key_name(key_diff) == name
    assert get_status(key_diff) == status
    assert get_old_value(key_diff) == ola_value
    assert get_value(key_diff) == value
    assert get_children(key_diff) == children
    assert is_changed_key(key_diff) == changed


expected_stylish_plain = read_fixture('stylish_plain_output.txt')
expected_stylish_nested = read_fixture('stylish_nested_output.txt')


def test_get_stylish():
    assert get_stylish(expected_diff_plain) == expected_stylish_plain
    assert get_stylish(expected_diff_nested) == expected_stylish_nested


input_nested_val = py_fixtures.NESTED_VAL
expected_nested_val = read_fixture('stringify_nested_output.txt')

stylish_val_cases = [(False, 'false'), (True, 'true'), (None, 'null'), ('', ''),
                     ('How are you?', 'How are you?'), (7, '7'),
                     (input_nested_val, expected_nested_val)]


@pytest.mark.parametrize('val, stylish_val', stylish_val_cases)
def test_to_stylish_val_primirives(val, stylish_val):
    assert to_stylish_val(val) == stylish_val


expected_plain = read_fixture('plain_output.txt')


def test_get_plain():
    assert get_plain(expected_diff_nested) == expected_plain


plain_val_cases = [(False, 'false'), (True, 'true'), (None, 'null'),
                   ('', "''"), ('Hello!', "'Hello!'"), (7, '7'),
                   (0, '0'), ({'a': 1, 'b': 1, 'c': 3}, '[complex value]')]


@pytest.mark.parametrize('val, plain_val', plain_val_cases)
def test_to_plain_val(val, plain_val):
    assert to_plain_val(val) == plain_val


@pytest.mark.parametrize('input', (expected_diff_plain, expected_diff_nested))
def test_get_json(input):
    assert get_json(input) == json.dumps(input)


gendiff_cases = [('file1.json', 'file2.json', 'stylish',
                  expected_stylish_plain),
                 ('file1_nested.json', 'file2_nested.json', 'plain',
                  expected_plain),
                 ('file1.json', 'file2.json', 'json',
                  json.dumps(expected_diff_plain))
                 ]


@pytest.mark.parametrize('file1, file2, format, result', gendiff_cases)
def test_generate_diff(file1, file2, format, result):
    assert generate_diff(file1, file2, format) == result
