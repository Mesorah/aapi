import requests
from pprint import pprint
_print = print

url = 'http://127.0.0.1:3001/users'

user_data = {
	"nome": "Luis Otávio",
	"password": "123456",
	"email": "luiz@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    # print(f'Texto {response.text}')
    print(f'JSON {response.json()}')
    # print(f'Bytes {response.content}')

else:
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Texto {response.text}')
    # print(f'Bytes {response.content}')