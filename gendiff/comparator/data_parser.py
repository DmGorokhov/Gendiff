import json
from yaml import safe_load


def read_file(filepath):
    if filepath.endswith('.json'):
        with open(filepath, 'r') as filedata:
            data = json.load(filedata)
    else:
        data = safe_load(open(filepath))
    return data
