def get_diff(old_data, new_data):

    def inner(old_data, new_data, diff):
        unique_keys = old_data.keys() | new_data.keys()
        for key in unique_keys:
            value_old = old_data.get(key, None)
            value_new = new_data.get(key, None)
            if isinstance(value_old, dict) and isinstance(value_new, dict):
                diff[key] = {'status': 'unchanged',
                             'children': inner(value_old, value_new, {})
                             }
            elif key not in old_data:
                diff[key] = {'status': 'added', 'value': value_new}
            elif key not in new_data:
                diff[key] = {'status': 'deleted', 'value': value_old}
            elif value_old == value_new:
                diff[key] = {'status': 'unchanged', 'value': value_old}
            else:
                diff[key] = {'status': 'changed',
                             'old_value': value_old, 'value': value_new
                             }
        return diff
    return inner(old_data, new_data, {})
