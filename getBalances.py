import requests
import json

# header
my_headers = {"content-type": "application/json","X-IOTA-API-Version": "1"}

# parematers
my_data = {"command": "getBalances","addresses": ["DE9DVSOWIIIKEBAAHCKBWNXGXTOKVLZPLRAGKZG9GXKFRFWERKBFYMPRLAGVZTRVYPEPHBMUPDMRQ9DPZ"],"threshold": 100}

# POST
r = requests.post('https://node.deviceproof.org:443', data = json.dumps(my_data), headers = my_headers)
print(r.text)