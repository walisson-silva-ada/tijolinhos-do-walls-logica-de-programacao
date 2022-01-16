jogadores = {}
jogadores_inativos = []

def cria_baralho():
    baralho = (['A'] + list(range(2,11)) + ['J', 'Q', 'K'])*4
    return baralho

def sorteio(baralho):
    import random
    sorteada = random.choice(baralho)
    baralho.remove(sorteada)
    print(f'Você comprou um {sorteada}.')
    return sorteada

def jogada(jogador, baralho):

    if jogador not in jogadores_inativos:
        print(f'\n{jogador}, é a sua vez de jogar!')
        print(f'Você tem {jogadores[jogador]} pontos.')
        opcao_de_compra = input('Deseja comprar uma carta? (Responda com sim ou nao) ').lower()
        
        if opcao_de_compra == 'nao' or opcao_de_compra == 'não':
            jogadores_inativos.append(jogador)
            
        else:
            sorteada = sorteio(baralho)
            if sorteada == 'A':
                jogadores[jogador] += 1
            elif sorteada in ['J', 'Q', 'K']:
                jogadores[jogador] += 10
            else:
                jogadores[jogador] += int(sorteada)
            
            if jogadores[jogador] > 21:
                jogadores_inativos.append(jogador)
                
    return jogadores, jogadores_inativos

def verificacao(jogadores):
    maior_pontuacao = 0
    vencedores = []
    for jogador in jogadores:
        if jogadores[jogador] > maior_pontuacao and jogadores[jogador] <= 21:
            maior_pontuacao = jogadores[jogador]
    
    for jogador in jogadores:
        if jogadores[jogador] == maior_pontuacao:
            vencedores.append(jogador)
    
    if len(vencedores) == 0:
        mensagem = 'NÃO HÁ GANHADORES. Todos os jogadores ultrapassaram 21 pontos!'
    elif len(vencedores) == 1:
        mensagem = f'{vencedores[0]} venceu com {maior_pontuacao} pontos.'
    else:
        mensagem = f'Houve um EMPATE. {vencedores} venceram com {maior_pontuacao} pontos.'
    
    return mensagem

def funcao_principal():
    numero_de_jogadores = int(input('Quantos jogadores vão participar? '))
    
    for jogador in range(numero_de_jogadores):
        nome = input(f'Qual o nome do {jogador+1}º jogador? ')
        jogadores[nome] = 0
        
    baralho = cria_baralho()
    
    while len(jogadores) != len(jogadores_inativos):
        for jogador in jogadores:
            jogada(jogador, baralho)
    
    if len(jogadores) == len(jogadores_inativos):
        mensagem = verificacao(jogadores)
    print(mensagem)
    return mensagem

funcao_principal()