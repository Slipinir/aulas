class Produto:
    def __init__(self, codigo, nome, referencia = '', estoque = 0):
        self.codigo = codigo
        self.nome = nome
        self.referencia = referencia
        self.estoque = estoque

    def incrementar_estoque(self, incremento = None):
        if not incremento:
            incremento = input('Digite o valor a ser incrementado ao estoque do produto: ')
        self.estoque += int(incremento)

    def quanto_tem_de_estoque(self):
        print(f'{self.nome} tem {self.estoque} de estoque')

produto = Produto(
    codigo=0,
    referencia='1762-1795',
    nome='Calça',
    estoque=5
)
produto.incrementar_estoque()
produto.quanto_tem_de_estoque()