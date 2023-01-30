def to_json_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def console_output(old_data, new_data, diff_result):
    OUTSET = '  '
    output = []
    for key, value in diff_result.items():
        if value == 'deleted':
            output.append(f'{OUTSET}- {key}: {to_json_str(old_data.get(key))}')
        elif value == 'added':
            output.append(f'{OUTSET}+ {key}: {to_json_str(new_data.get(key))}')
        elif value == 'unchanged':
            output.append(f'{OUTSET * 2}{key}: '
                          f'{to_json_str(new_data.get(key))}')
        else:
            output.append(f'{OUTSET}- {key}: {to_json_str(old_data.get(key))}')
            output.append(f'{OUTSET}+ {key}: {to_json_str(new_data.get(key))}')

    output = '{\n' + '\n'.join(output) + '\n}'
    return output


def get_diff(old_data, new_data):
    unique_keys = sorted(old_data.keys() | new_data.keys())

    diff_result = {}
    for key in unique_keys:
        if key not in old_data:
            diff_result[key] = 'added'
        elif key not in new_data:
            diff_result[key] = 'deleted'
        elif old_data[key] == new_data[key]:
            diff_result[key] = 'unchanged'
        else:
            diff_result[key] = 'changed'

    return diff_result
