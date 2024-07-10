from avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []

    # construtor
    def __init__(self, nome, categoria, capacidade):
        self._nome = nome
        self.categoria = categoria.upper()
        self._ativo = False #atributo PROTEGIDO
        self.capacidade = str(capacidade)
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) #toda vez cria um objeto e insere na lista restaurantes

    #self => referencia da instancia atual que estamos utilizando no momento
    def __str__(self):
        return f'{self.nome.ljust(20)}'

    @classmethod #BOA PRÁTICA - para indicar que é um metodo da classe
    def listar_restaurantes(cls):
        print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Capacidade".ljust(20)} | {"Nota".ljust(19)} '
              f'| Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | '
                  f'{restaurante.capacidade.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)}| {restaurante.ativo}')

    def alternar_estado(self):
        self._ativo = not self._ativo #para trocar o estado do Ativo

    #@property
    #def nota_avaliacao(self):
    #    return '★' * self._nota_avaliacao

    @property #para modificar como o atributo será lido
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def receber_avaliacao(self, cliente, nota):
        if nota > 5:
            nota = 5
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 'Sem avaliação'
        soma_notas = sum(Avaliacao._nota for Avaliacao in self._avaliacao) #para cada avaliacao dentro do ._avaliacao, pega a ._nota
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)
        return media

    #def adicionar_bebida_no_cardapio(self, bebida):
    #    self._cardapio.append(bebida) #pego o cardapio e adiciono a bebida

    #def adicionar_prato_no_cardapio(self, prato):
    #    self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): # V - se item for derivado da classe ItemCardapio
            self._cardapio.append(item)

    def exibir_cardapio(self):
        print(f'Cardápio do restaurante: {self._nome}\n')
        for i, item in enumerate(self._cardapio, start = 1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Descrição: {item.descricao} | Preço: R$ {item._preco:.2f} '
                print (mensagem_prato)
            #hasattr - para saber se classe tem determinado atributo
            else:
                mensagem_bebida = (f'{i}. Nome: {item._nome} | Tamanho: {item.tamanho} | Preço: R$'
                                   f' {item._preco:.2f} ')
                print (mensagem_bebida)
#restaurante_praca = Restaurante('Bistrô', 'Italiana', 100, 5)
#restaurante_praca.alternar_estado()

#restaurante_pizza = Restaurante('Pizza Place', 'Fast Food', 55, 3)

#vars => utilizado para imprimir os atributos da classe
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))

# print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)}')
# print(restaurante_praca)
# print(restaurante_pizza)

#Restaurante.listar_restaurantes()


