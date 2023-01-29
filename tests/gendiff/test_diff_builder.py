from gendiff import generate_diff
from tests.gendiff.comparator.test_diff_counter import read


filepath_old = 'tests/fixtures/file1.json'
filepath_new = 'tests/fixtures/file2.json'


def test_generate_diff():
    expected_output = read('tests/fixtures/plain_output.txt')
    diff_output = generate_diff(filepath_old, filepath_new)
    
    assert diff_output == expected_output