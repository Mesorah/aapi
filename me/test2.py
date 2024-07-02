import requests

def poke_api(nome):
    url = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    resposta = requests.get(url=url)

    if resposta.status_code >= 200 and resposta.status_code <= 299:
        pokemon_stats = resposta.json()

        caracteristicas = [pokemon_stats['name'],
                           pokemon_stats['height'],
                           pokemon_stats['weight'],
                           ]
        
        return caracteristicas

    else:
        print('erro')
        print(resposta.status_code)

nome_pokemon = input('Digite o nome do pokemon: ').lower()

test = poke_api(nome_pokemon)


if test:
    print(test)

else:
    print('error')