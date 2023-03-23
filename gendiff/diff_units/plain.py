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
        case _:
            return f"'{value}'"


def get_plain(diff):
    STATUS_TO_WORD = {'deleted': 'removed',
                      'added': 'added',
                      'changed': 'updated'
                      }

    def inner(diff, path):
        lines = []
        for key, key_diff in sorted(diff.items()):
            current_path = f"{path}{key}"
            key_status = key_diff.get('status')
            line = (f"Property '{current_path}' was "
                    f"{STATUS_TO_WORD.get(key_status)}")

            if not key_diff.get('children'):
                value = to_plain_val(key_diff.get('value'))

                match key_status:
                    case 'deleted':
                        lines.append(line)
                    case 'added':
                        line += f" with value: {value}"
                        lines.append(line)
                    case 'changed':
                        old_value = to_plain_val(key_diff.get('old_value'))
                        line += f". From {old_value} to {value}"
                        lines.append(line)
            else:
                children = key_diff.get('children')
                lines.append(inner(children, current_path + '.'))
        return '\n'.join(lines)

    return inner(diff, '')
