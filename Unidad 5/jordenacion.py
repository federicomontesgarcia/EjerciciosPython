import json

data = {
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17}

print(json.dumps(data, sort_keys=True))