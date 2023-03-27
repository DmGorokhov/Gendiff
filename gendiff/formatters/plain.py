from gendiff.diff_units.data_comparator import (get_key_name, get_children,
                                                get_value, get_old_value,
                                                get_status, is_changed_key
                                                )


def to_plain_val(value):
    match value:
        case bool(value):
            return str(value).lower()
        case dict(value):
            return '[complex value]'
        case None:
            return 'null'
        case '':
            return "''"
        case str(value):
            return f"'{value}'"
        case _:
            return f"{value}"


def get_plain(diff):

    def inner(key_diff, path=''):
        key_name = get_key_name(key_diff)
        key_status = get_status(key_diff)
        nested_keys = get_children(key_diff)

        current_path = f"{path}{key_name}"
        if not nested_keys:
            line = (f"Property '{current_path}' was {key_status}")
            value = to_plain_val(get_value(key_diff))
            match key_status:
                case 'added':
                    line += f" with value: {value}"
                case 'updated':
                    old_value = to_plain_val(get_old_value(key_diff))
                    line += f". From {old_value} to {value}"
            return line

        current_path += '.'
        changed_keys = filter(is_changed_key, nested_keys)

        lines = map(lambda key: inner(key, current_path), changed_keys)
        result = '\n'.join(lines)
        return result

    plain_diff = '\n'.join(map(inner, diff))
    return plain_diff
