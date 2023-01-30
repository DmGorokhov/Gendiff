import json
from yaml import safe_load


def read_file(filepath):

    if filepath.endswith('.json'):
        return json.load(open(filepath))
    else:
        return safe_load(open(filepath))
