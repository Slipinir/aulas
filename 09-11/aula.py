def print_meu_nome():
    print('Luiz Carlos Mendonça Júnior')

def retorna_1(numero):
    if numero == 1:
        return 1
    else:
        return 2

def retorna(variavel):
    if variavel == 's':
        return 's'
    elif variavel == 1:
        return 1
    else:
        return None

print_meu_nome()
print('é programador na Alternativa Sistemas')
print_meu_nome()
print('é de Pirajuí/SP')
print_meu_nome()
idade = input('Quantos anos você tem? ')
if int(idade) >= 18:
    print(f'Com {idade} anos você pode tirar carta')
    print('Já pode dirigir')
elif int(idade) >= 25:
    print('Pode ter arma')
else:
    print(f'Com {idade} você não pode tirar cartar e nem ter arma')
