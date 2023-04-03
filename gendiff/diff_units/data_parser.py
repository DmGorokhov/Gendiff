import json
from yaml import safe_load


def read_file(filepath):
    with open(filepath, 'r') as filedata:
        if filepath.endswith('.json'):
            data = json.load(filedata)
        elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
            data = safe_load(filedata)
        else:
            raise Exception('Files should be json or yaml format')
    return data
