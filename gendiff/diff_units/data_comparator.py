def get_diff(old_data, new_data):

    def make_key_diff(key):
        value_old = old_data.get(key, None)
        value_new = new_data.get(key, None)
        key_diff = (key, ['unchanged', value_old, value_new, None])

        if key not in old_data:
            key_diff[1][0] = 'added'
        elif key not in new_data:
            key_diff[1][0] = 'removed'
        elif isinstance(value_old, dict) and isinstance(value_new, dict):
            key_diff[1][3] = get_diff(value_old, value_new)
            key_diff[1][1], key_diff[1][2] = [None, None]
        elif value_old != value_new:
            key_diff[1][0] = 'updated'
        else:
            key_diff[1][1] = None
        return key_diff

    unique_keys = sorted(old_data.keys() | new_data.keys())
    diff = list(map(make_key_diff, unique_keys))

    return diff


def get_key_name(key_diff):
    return key_diff[0]


def get_status(key_diff):
    return key_diff[1][0]


def get_children(key_diff):
    return key_diff[1][3]


def get_value(key_diff):
    if get_status(key_diff) == 'removed':
        return key_diff[1][1]
    return key_diff[1][2]


def get_old_value(key_diff):
    return key_diff[1][1]


def is_changed_key(key_diff):
    if get_status(key_diff) != 'unchanged' or get_children(key_diff):
        return True
    return False
