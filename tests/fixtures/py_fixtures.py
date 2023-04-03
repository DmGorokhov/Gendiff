EXPECTED_DIFF = [('follow', ['removed', False, None, None]),
                 ('host', ['unchanged', None, 'hexlet.io', None]),
                 ('proxy', ['removed', '123.234.53.22', None, None]),
                 ('timeout', ['updated', 50, 20, None]),
                 ('verbose', ['added', None, True, None])]

NOT_CHANGED = [('follow', ['unchanged', None, False, None]),
               ('host', ['unchanged', None, 'hexlet.io', None]),
               ('proxy', ['unchanged', None, '123.234.53.22', None]),
               ('timeout', ['unchanged', None, 50, None])]

EXPECTED_DIFF_NESTED = (
    [('common', ['unchanged', None, None, [
        ('follow', ['added', None, False, None]),
        ('setting1', ['unchanged', None, 'Value 1', None]),
        ('setting2', ['removed', 200, None, None]),
        ('setting3', ['updated', True, None, None]),
        ('setting4', ['added', None, 'blah blah', None]),
        ('setting5', ['added', None, {'key5': 'value5'}, None]),
        ('setting6', ['unchanged', None, None, [
            ('doge', ['unchanged', None, None, [
                ('wow', ['updated', '', 'so much', None])]]),
            ('key', ['unchanged', None, 'value', None]),
            ('ops', ['added', None, 'vops', None])]])]]),
     ('group1', ['unchanged', None, None, [
         ('baz', ['updated', 'bas', 'bars', None]),
         ('foo', ['unchanged', None, 'bar', None]),
         ('nest', ['updated', {'key': 'value'}, 'str', None])]]),
     ('group2', ['removed', {'abc': 12345, 'deep': {'id': 45}}, None, None]),
     ('group3', ['added', None, {'deep': {'id': {'number': 45}},
                                 'fee': 100500}, None])])

NESTED_VAL = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": 'value',
            "number": 5,
            None: "None",
        },
    },
}
