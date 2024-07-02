import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
requisicao = requisicao.json()
requisicao_dolar = requisicao['USDBRL']['bid']
print(requisicao)
print(requisicao_dolar)