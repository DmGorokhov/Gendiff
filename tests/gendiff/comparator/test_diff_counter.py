import json

from gendiff.comparator.diff_counter import get_diff, to_json_str, console_output


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


data1 = json.load(open('tests/fixtures/file1.json'))
data2 = json.load(open('tests/fixtures/file2.json'))

expected_diff = {'follow': 'deleted', 'host': 'unchanged', 
                 'proxy': 'deleted', 'timeout': 'changed', 
                 'verbose': 'added'}

not_changed = {'follow': 'unchanged', 'host': 'unchanged', 
                'proxy': 'unchanged', 'timeout': 'unchanged'}
    

def test_to_json_str():
    assert to_json_str(False) == 'false'
    assert to_json_str('false') == 'false'
    assert to_json_str(True) == 'true'
    assert to_json_str('true') == 'true'
    assert to_json_str(None) == 'null'
    assert to_json_str('') == ''
    assert to_json_str('How are you?') == 'How are you?'
    assert to_json_str(7) == '7'


def test_get_diff():
    diff = get_diff(data1, data2)
    nothing_diff = get_diff(data1, data1)
    
    assert diff == expected_diff
    assert nothing_diff == not_changed

def test_console_output():
    expected_output = read('tests/fixtures/plain_output.txt')
    output = console_output(data1, data2, get_diff(data1, data2))
    
    assert output == expected_output