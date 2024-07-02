import requests

# requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# print(requisicao.json())


# requisicao = requests.get('https://test-cc3df-default-rtdb.firebaseio.com/.json')
# print(requisicao.json())


# informacoes = '{"nome": "SLA KK"}'
# requisicao = requests.post('https://test-cc3df-default-rtdb.firebaseio.com/.json', data=informacoes)
# print(requisicao)

# informacoes = '{"nome": "Curinthia", "sla": "k"}'
# requisicao = requests.patch('https://test-cc3df-default-rtdb.firebaseio.com/-O0p4OhUGXYxYKTWamkU/.json', data=informacoes)
# print(requisicao)

requisicao = requests.delete('https://test-cc3df-default-rtdb.firebaseio.com/-O0p408ylZc-AGj5nElO.json')
print(requisicao)

#usar o /. ou só .