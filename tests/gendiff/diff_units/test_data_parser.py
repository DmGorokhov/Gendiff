import json
from yaml import safe_load
from gendiff.diff_units.data_parser import read_file


expected_data1_plain = {"host": "hexlet.io", "timeout": 50, 
                        "proxy": "123.234.53.22", "follow": False}
expected_data2_plain = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
expected_data3_nested = {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}
expected_data4_nested = {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}


data1_path_json = 'tests/fixtures/file1.json'
data2_path_json = 'tests/fixtures/file2.json'
data1_path_yaml = 'tests/fixtures/file1.yaml'
data2_path_yaml = 'tests/fixtures/file2.yaml'
data3_path_json = 'tests/fixtures/file1_nested.json'
data4_path_json = 'tests/fixtures/file2_nested.json'
data3_path_yaml = 'tests/fixtures/file1_nested.yaml'
data4_path_yaml = 'tests/fixtures/file2_nested.yaml'


def test_read_file():
    assert read_file(data1_path_json) == expected_data1_plain
    assert read_file(data2_path_json) == expected_data2_plain
    assert read_file(data1_path_yaml) == expected_data1_plain
    assert read_file(data2_path_yaml) == expected_data2_plain
    assert read_file(data3_path_json) == expected_data3_nested
    assert read_file(data4_path_json) == expected_data4_nested
    assert read_file(data3_path_yaml) == expected_data3_nested
    assert read_file(data4_path_yaml) == expected_data4_nested
