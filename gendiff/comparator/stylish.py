from itertools import chain


STATUS_SIGNS = {'deleted': '- ',
                'added': '+ ',
                'unchanged': '  ',
                'changed': '+ '
                }
REPLACER = ' '
IDENT_STEP = 4
BACKSPACE_STEP = 2


def make_style_val(value, depth=0):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        return str(value)
    items = []
    for key, val in value.items():
        key_ident = IDENT_STEP * REPLACER * (depth + 1)
        items.append(f'{key_ident}{key}: {make_style_val(val, depth+1)}')

    brace_outset = IDENT_STEP * REPLACER * depth
    result = chain("{", items, [brace_outset + "}"])
    return '\n'.join(result)


def get_stylish(diff):

    def inner(diff, depth):
        lines = []
        ident = (IDENT_STEP * depth - BACKSPACE_STEP) * REPLACER
        for key, key_diff in sorted(diff.items()):
            key_status = key_diff.get('status')
            output_key = f'{ident}{STATUS_SIGNS.get(key_status)}{key}'

            if not key_diff.get('children'):
                if key_status == 'changed':
                    old_output_key = f'{ident}- {key}'
                    old_value = make_style_val(key_diff.get('old_value'), depth)
                    lines.append(f'{old_output_key}: {old_value}')
                value = make_style_val(key_diff.get('value'), depth)
                lines.append(f'{output_key}: {value}')
            else:
                children = key_diff.get('children')
                lines.append(f'{output_key}: {inner(children, depth+1)}')

        bottom_outset = (IDENT_STEP * depth - IDENT_STEP) * REPLACER
        result = chain("{", lines, [bottom_outset + "}"])
        return '\n'.join(result)

    return inner(diff, 1)
