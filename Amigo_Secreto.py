nome_presentes = {'iara': ('mochila', 'estojo', 'lapis'), 'adelar': ('sapato', 'camisa', 'carteira'), 'jessica': ('agenda', 'bolsa', 'brincos'), 'jocelina': ('xicara', 'meias', 'perfume'), 'elaine': ('sandalia', 'sapatilha', 'camiseta')}

nome = input('Informe o nome de seu amigo: ').lower()

while nome not in nome_presentes:
    print('Este nome não está na lista!!!')
    print('Lista de amigos possíveis:', nome_presentes.keys())
    nome = input('Informe um nome da lista acima: ').lower()

presente = input(f'Que presente gostaria de dar para {nome.capitalize()}? ').lower()

if presente in nome_presentes[nome]:
    print('Uhul! Seu amigo secreto vai adorar o/')
else:
    print('Tente Novamente!')