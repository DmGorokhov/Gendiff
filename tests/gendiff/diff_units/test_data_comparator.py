import json
from gendiff.diff_units.data_comparator import (get_diff, get_key_name, 
                                                get_children, get_value, 
                                                get_old_value, get_status, 
                                                is_changed_key
                                                )
from gendiff.diff_units.data_parser import read_file


data1_json = read_file('tests/fixtures/file1.json')
data2_json = read_file('tests/fixtures/file2.json')
data1_json_nested = read_file('tests/fixtures/file1_nested.json')
data2_json_nested = read_file('tests/fixtures/file2_nested.json')
data1_yaml = read_file('tests/fixtures/file1.yaml')
data2_yaml = read_file('tests/fixtures/file2.yaml')
data1_yaml_nested = read_file('tests/fixtures/file1_nested.yaml')
data2_yaml_nested = read_file('tests/fixtures/file2_nested.yaml')


expected_diff = [('follow', ['removed', False, None, None]), 
                 ('host', ['unchanged', None, 'hexlet.io', None]),
                 ('proxy', ['removed', '123.234.53.22', None, None]),
                 ('timeout', ['updated', 50, 20, None]), 
                 ('verbose', ['added', None, True, None])] 
                  
               

not_changed = [('follow', ['unchanged', None, False, None]), 
               ('host', ['unchanged', None, 'hexlet.io', None]),
               ('proxy', ['unchanged', None, '123.234.53.22', None]),
               ('timeout', ['unchanged', None, 50, None])]
               
expected_diff_nested = (
[('common', ['unchanged', None, None, 
   [('follow', ['added', None, False, None]), 
    ('setting1', ['unchanged', None, 'Value 1', None]), 
    ('setting2', ['removed', 200, None, None]), 
    ('setting3', ['updated', True, None, None]), 
    ('setting4', ['added', None, 'blah blah', None]), 
    ('setting5', ['added', None, {'key5': 'value5'}, None]), 
    ('setting6', ['unchanged', None, None, 
         [('doge', ['unchanged', None, None, 
               [('wow', ['updated', '', 'so much', None])]]), 
          ('key', ['unchanged', None, 'value', None]), 
          ('ops', ['added', None, 'vops', None])]])]]), 
 ('group1', ['unchanged', None, None, 
    [('baz', ['updated', 'bas', 'bars', None]), 
          ('foo', ['unchanged', None, 'bar', None]), 
          ('nest', ['updated', {'key': 'value'}, 'str', None])]]), 
 ('group2', ['removed', {'abc': 12345, 'deep': {'id': 45}}, None, None]), 
 ('group3', ['added', None, {'deep': {'id': {'number': 45}}, 'fee': 100500}, None])])


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


key_diff = ('group1', ['unchanged', None, None, 'we are children'])
key_diff2 = ('group2', ['unchanged', None, 2023, None])
key_diff3 = ('group3', ['updated', 'young', 'old', None])
key_diff4 = ('group4', ['removed', False, None, None])
key_diff5 = ('group5', ['added', None, 0, None])
key_diff6 = ('group6', ['unchanged', None, {'a': 2, 'g': 'gh'}, None])


def test_get_key_name():
    assert get_key_name(key_diff) == 'group1'
    assert get_key_name(key_diff2) == 'group2'
    assert get_key_name(key_diff3) == 'group3'
    assert get_key_name(key_diff4) == 'group4'
    assert get_key_name(key_diff5) == 'group5'
    assert get_key_name(key_diff6) == 'group6'


def test_get_status():
    assert get_status(key_diff) == 'unchanged'
    assert get_status(key_diff2) == 'unchanged'
    assert get_status(key_diff3) == 'updated'
    assert get_status(key_diff4) == 'removed'
    assert get_status(key_diff5) == 'added'
    assert get_status(key_diff6) == 'unchanged'


def test_get_children():
    assert get_children(key_diff) == 'we are children'
    assert get_children(key_diff2) == None
    assert get_children(key_diff3) == None
    assert get_children(key_diff4) == None
    assert get_children(key_diff5) == None
    assert get_children(key_diff6) == None


def test_get_value():
   assert get_value(key_diff) == None
   assert get_value(key_diff2) == 2023
   assert get_value(key_diff3) == 'old'
   assert get_value(key_diff4) == False
   assert get_value(key_diff5) == 0
   assert get_value(key_diff6) == {'a': 2, 'g': 'gh'}


def test_get_old_value():
    assert get_old_value(key_diff) == None
    assert get_old_value(key_diff2) == None
    assert get_old_value(key_diff3) == 'young'
    assert get_old_value(key_diff4) == False
    assert get_old_value(key_diff5) == None
    assert get_old_value(key_diff6) == None


def test_is_changed_key():
    assert is_changed_key(key_diff) == True
    assert is_changed_key(key_diff2) == False
    assert is_changed_key(key_diff3) == True
    assert is_changed_key(key_diff4) == True
    assert is_changed_key(key_diff5) == True
    assert is_changed_key(key_diff6) == False