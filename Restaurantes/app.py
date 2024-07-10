import requests
import json
from restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
        })

else:
    print(f'Erro: {response.status_code}')

#print(dados_restaurante['McDonald’s'])

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)


#restaurante_praca = Restaurante('Praça', 'Gourmet', 100)
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana', 50)
#restaurante_japones = Restaurante('Sushi Food', 'Japonesa', 45)

#restaurante_praca.receber_avaliacao('Guilherme', 10)
#restaurante_praca.receber_avaliacao('Talita', 4)
#restaurante_praca.receber_avaliacao('João', 4)
#restaurante_mexicano.alternar_estado()

#bebida_suco = Bebida('Suco de Melancia', 7, 'grande')
#prato_paozinho = Prato ('Paozinho', 2.50, 'O melhor pão da cidade.')

#restaurante_praca.adicionar_no_cardapio(bebida_suco)
#restaurante_praca.adicionar_no_cardapio(prato_paozinho)


#def main():
    #Restaurante.listar_restaurantes()
    #restaurante_praca.exibir_cardapio()
    #print('======')
    #bebida_suco.aplicar_desconto()
    #prato_paozinho.aplicar_desconto()
    #restaurante_praca.exibir_cardapio()

#if __name__ == '__main__':
    #main()