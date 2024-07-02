import requests
from pprint import pprint
from get_token import token

url = 'http://127.0.0.1:3001/alunos/2'

headers = {
    'Authorization': token
}

aluno_data = {
	# "nome": "Let",
	# "sobrenome": "Vieira",
	# "email": "luana2@email.com",
	# "idade": "50",
	# "peso": "80.04",
	# "altura": "1.90"
}

response = requests.delete(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    # print(f'Texto {response.text}')

    response_data = response.json()
    print(response_data)

    # print(f'JSON {response.json()}') 
    # print(f'Bytes {response.content}')

else:
    print(f'Status Code {response.status_code}')
    print(f'Reason {response.reason}')
    print(f'Texto {response.text}')
    # print(f'Bytes {response.content}')