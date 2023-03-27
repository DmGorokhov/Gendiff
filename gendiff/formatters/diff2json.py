import json

from gendiff.diff_units.data_comparator import (get_key_name, get_children,
                                                get_value, get_old_value,
                                                get_status
                                                )


def get_json(diff):
    data = {}

    def walk(key_diff):
        key_name = get_key_name(key_diff)
        key_status = get_status(key_diff)
        nested_keys = get_children(key_diff)
        key_diff_json = {}
        if not nested_keys:
            value = get_value(key_diff)
            key_diff_json[key_name] = {'status': key_status, 'value': value}
            if key_status == 'updated':
                key_diff_json[key_name]['old_value'] = get_old_value(key_diff)
            return key_diff_json
        key_diff_json[key_name] = {'status': key_status,
                                   'children': list(map(walk, nested_keys))
                                   }
        return key_diff_json
    for node in diff:
        data.update(walk(node))

    with open('diff_report.json', 'w') as file:
        file = json.dumps(data)
    return file
