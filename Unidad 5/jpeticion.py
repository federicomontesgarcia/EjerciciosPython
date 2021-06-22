import json
import requests

resp = requests.get('http://ip-api.com/json/208.80.152.201')
print(json.loads(resp.content))

data = {'first_name': 'Daniel', 'last_name': 'Rodríguez'}
print(json.dumps(data))
print(json.dumps(data, ensure_ascii=False))