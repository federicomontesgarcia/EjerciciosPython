import json
import requests

data = {'first_name': 'Daniel', 'last_name': 'Rodríguez'}
print(json.dumps(data))
print(json.dumps(data, ensure_ascii=False))