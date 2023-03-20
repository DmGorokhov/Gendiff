import json

from gendiff.comparator.diff_counter import get_diff


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


data1 = json.load(open('tests/fixtures/file1.json'))
data2 = json.load(open('tests/fixtures/file2.json'))
data1_nested = json.load(open('tests/fixtures/file1_nested.json'))
data2_nested = json.load(open('tests/fixtures/file2_nested.json'))

expected_diff = {'follow': {'status': 'deleted', 'value': False}, 
                 'host': {'status': 'unchanged', 'value': 'hexlet.io'},
                 'verbose': {'status': 'added', 'value': True}, 
                 'timeout': {'status': 'changed', 'old_value': 50, 'value': 20}, 
                 'proxy': {'status': 'deleted', 'value': '123.234.53.22'}}

not_changed = {'follow': {'status': 'unchanged', 'value': False}, 
               'host': {'status': 'unchanged', 'value': 'hexlet.io'},
               'timeout': {'status': 'unchanged', 'value': 50}, 
               'proxy': {'status': 'unchanged', 'value': '123.234.53.22'}}

expected_diff_nested = {'group1': {'status': 'unchanged', 'children': 
                            {'baz': {'status': 'changed', 'old_value': 'bas', 'value': 'bars'}, 
                             'nest': {'status': 'changed', 'old_value': {'key': 'value'}, 'value': 'str'}, 
                             'foo': {'status': 'unchanged', 'value': 'bar'}}}, 
                        'group3': {'status': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}, 
                        'group2': {'status': 'deleted', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 
                        'common': {'status': 'unchanged', 'children': 
                            {'setting5': {'status': 'added', 'value': {'key5': 'value5'}}, 
                             'setting3': {'status': 'changed', 'old_value': True, 'value': None}, 
                             'follow': {'status': 'added', 'value': False}, 
                             'setting6': {'status': 'unchanged', 'children': 
                                    {'ops': {'status': 'added', 'value': 'vops'}, 
                                     'key': {'status': 'unchanged', 'value': 'value'}, 
                                     'doge': {'status': 'unchanged', 'children': 
                                              {'wow': {'status': 'changed', 'old_value': '', 'value': 'so much'}}}}}, 
                             'setting1': {'status': 'unchanged', 'value': 'Value 1'}, 
                             'setting2': {'status': 'deleted', 'value': 200}, 
                             'setting4': {'status': 'added', 'value': 'blah blah'}}}}


    

"""def test_to_json_str():
    assert to_json_str(False) == 'false'
    assert to_json_str('false') == 'false'
    assert to_json_str(True) == 'true'
    assert to_json_str('true') == 'true'
    assert to_json_str(None) == 'null'
    assert to_json_str('') == ''
    assert to_json_str('How are you?') == 'How are you?'
    assert to_json_str(7) == '7'
"""

def test_get_diff():
    diff_plain = get_diff(data1, data2)
    nothing_diff = get_diff(data1, data1)
    diff_nested = get_diff(data1_nested, data2_nested)
    
    assert diff_plain == expected_diff
    assert nothing_diff == not_changed
    assert diff_nested == expected_diff_nested
