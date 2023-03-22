import json
from yaml import safe_load


def read_file(filepath):
    with open(filepath, 'r') as filedata:
        if filepath.endswith('.json'):
            data = json.load(filedata)
        else:
            data = safe_load(filedata)
    return data
