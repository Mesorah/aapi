import requests

def chama_api(valores={}):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url, params=valores)

    if response.status_code == 200:
        return response.json()
    
    else:
        return None

test = chama_api({'id': 4})

if test:
    print(test)
else:
    print('Erro ao chamar a API')
