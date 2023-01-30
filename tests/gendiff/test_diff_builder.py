from gendiff import generate_diff


filepath_old = 'tests/fixtures/file1.json'
filepath_new = 'tests/fixtures/file2.json'


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

def test_generate_diff():
    expected_output = read('tests/fixtures/plain_output.txt')
    diff_output = generate_diff(filepath_old, filepath_new)
    
    assert diff_output == expected_output