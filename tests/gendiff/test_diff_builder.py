from gendiff.diff_builder import generate_diff


filepath_old_plain = 'tests/fixtures/file1.json'
filepath_new_plain = 'tests/fixtures/file2.json'
filepath_old_nested = 'tests/fixtures/file1_nested.json'
filepath_new_nested = 'tests/fixtures/file2_nested.json'


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

def test_generate_diff():
    expected_output_plain = read('tests/fixtures/plain_output.txt')
    expected_output_nested = read('tests/fixtures/nested_output.txt')

    diff_output_plain = generate_diff(filepath_old_plain, filepath_new_plain)
    diff_output_nested = generate_diff(filepath_old_nested, filepath_new_nested)
    
    assert diff_output_plain == expected_output_plain
    assert diff_output_nested == expected_output_nested
