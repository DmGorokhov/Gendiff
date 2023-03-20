import json
from yaml import safe_load
from gendiff.comparator.data_parser import read_file


data1_json = json.load(open('tests/fixtures/file1.json'))
data2_json = json.load(open('tests/fixtures/file2.json'))
data1_json_nested = json.load(open('tests/fixtures/file1_nested.json'))
data2_json_nested = json.load(open('tests/fixtures/file2_nested.json'))
data1_yml = safe_load(open('tests/fixtures/file1.yaml'))
data2_yml = safe_load(open('tests/fixtures/file2.yml'))


def test_read_file():
    assert read_file('tests/fixtures/file1.json') == data1_json
    assert read_file('tests/fixtures/file2.json') == data2_yml
    assert read_file('tests/fixtures/file1.yaml') == data1_json
    assert read_file('tests/fixtures/file2.yml') == data2_yml
    assert read_file('tests/fixtures/file1_nested.json') == data1_json_nested
    assert read_file('tests/fixtures/file2_nested.json') == data2_json_nested


