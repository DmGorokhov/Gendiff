import json


def to_json_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def read_file(filepath):
    return json.load(open(filepath))


def generate_diff(filepath_1, filepath_2):
    OUTSET = '  '

    old_data = read_file(filepath_1)
    new_data = read_file(filepath_2)

    common_keys = old_data.keys() & new_data.keys()
    deleted_keys = old_data.keys() - new_data.keys()
    added_keys = new_data.keys() - old_data.keys()
    keys_diff = sorted(common_keys | deleted_keys | added_keys)

    diff_result = []
    for key in keys_diff:
        if key in deleted_keys:
            diff_result.append(f'{OUTSET}- {key}: '
                               f'{to_json_str(old_data.get(key))}')
        elif key in added_keys:
            diff_result.append(f'{OUTSET}+ {key}: '
                               f'{to_json_str(new_data.get(key))}')
        elif old_data.get(key) == new_data.get(key):
            diff_result.append(f'{OUTSET * 2}{key}: '
                               f'{to_json_str(new_data.get(key))}')
        else:
            diff_result.append(f'{OUTSET}- {key}: '
                               f'{to_json_str(old_data.get(key))}')
            diff_result.append(f'{OUTSET}+ {key}: '
                               f'{to_json_str(new_data.get(key))}')

    output = '{\n' + '\n'.join(diff_result) + '\n}'
    return output
