import requests
from pprint import pprint
_print = print

url = 'http://127.0.0.1:3001/tokens'

user_data = {
	"password": "123456",
	"email": "luiz@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    # print(f'Texto {response.text}')

    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)

    # print(f'JSON {response.json()}')
    # print(f'Bytes {response.content}')

else:
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Texto {response.text}')
    # print(f'Bytes {response.content}')