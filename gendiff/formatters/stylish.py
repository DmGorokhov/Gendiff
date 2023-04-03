from itertools import chain
from gendiff.diff_units.data_comparator import (get_key_name, get_children,
                                                get_value, get_old_value,
                                                get_status
                                                )


def to_stylish_val(value, depth=0):
    val_replacer = ' '
    val_ident_step = 4

    match value:
        case bool(value):
            return str(value).lower()
        case None:
            return 'null'
        case dict(value):
            items = []
            for key, val in value.items():
                key_ident = val_ident_step * val_replacer * (depth + 1)
                items.append(f'{key_ident}{key}: '
                             f'{to_stylish_val(val, depth+1)}')
            brace_outset = val_ident_step * val_replacer * depth
            stylish_str = chain("{", items, [brace_outset + "}"])
            return '\n'.join(stylish_str)
    return str(value)


def get_stylish(diff):
    status_signs = {'removed': '- ', 'added': '+ ',
                    'unchanged': '  ', 'updated': '+ '
                    }
    replacer = ' '
    ident_step = 4
    backspace_step = 2

    def inner(key_diff, depth=1):
        key_name = get_key_name(key_diff)
        key_status = get_status(key_diff)
        nested_keys = get_children(key_diff)

        ident = (ident_step * depth - backspace_step) * replacer
        stylish_status = status_signs.get(key_status)

        stylish_key = f'{ident}{stylish_status}{key_name}: '

        if not nested_keys:
            line = ''
            if key_status == 'updated':
                line += f'{ident}- {key_name}: '
                old_value = get_old_value(key_diff)
                line += to_stylish_val(old_value, depth) + '\n'
            value = get_value(key_diff)
            line += f'{stylish_key}{to_stylish_val(value, depth)}'
            return line

        depth += 1
        nested_lines = '\n'.join(map(lambda key:
                                     inner(key, depth), nested_keys))
        bottom_outset = (ident_step * depth - ident_step) * replacer + '}'
        result = '\n'.join((stylish_key + '{', nested_lines, bottom_outset))
        return result

    stylish_diff = '\n'.join(map(inner, diff))

    return '\n'.join(("{", stylish_diff, "}"))
