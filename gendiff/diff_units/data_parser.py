import json
from yaml import safe_load


def get_format(filepath):
    if filepath.endswith('.json'):
        format = 'json'
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        format = 'yaml'
    else:
        format = 'other format'
    return format


def parse_json(filepath):
    with open(filepath, 'r') as filedata:
        data = json.load(filedata)
    return data


def parse_yaml(filepath):
    with open(filepath, 'r') as filedata:
        data = safe_load(filedata)
    return data


def read_file(filepath):
    format = get_format(filepath)

    match format:
        case 'json':
            parsed_data = parse_json(filepath)
        case 'yaml':
            parsed_data = parse_yaml(filepath)
        case 'other format':
            raise Exception('Files should be json or yaml format')
    return parsed_data
