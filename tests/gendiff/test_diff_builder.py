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
    expected_stylish_plain = read('tests/fixtures/stylish_plain_output.txt')
    expected_stylish_nested = read('tests/fixtures/stylish_nested_output.txt')
    expected_plain_output = read('tests/fixtures/plain_output.txt')

    diff_default_plain = generate_diff(filepath_old_plain, filepath_new_plain)
    diff_default_nested = generate_diff(filepath_old_nested, filepath_new_nested)

    diff_stylish_plain = generate_diff(filepath_old_plain, filepath_new_plain, 'stylish')
    diff_stylish_nested = generate_diff(filepath_old_nested, filepath_new_nested, 'stylish')
    diff_plain = generate_diff(filepath_old_nested, filepath_new_nested, 'plain')

    assert diff_stylish_plain == expected_stylish_plain
    assert diff_stylish_nested == expected_stylish_nested
    assert diff_plain == expected_plain_output
    assert diff_default_plain == expected_stylish_plain
    assert diff_default_nested == expected_stylish_nested
