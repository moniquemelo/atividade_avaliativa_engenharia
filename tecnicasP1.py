from random import randint

interacoes = 0
sala = 1
while interacoes < 7 and sala != 9:
    print(f'Você está na sala: {sala}')
    sala += int(input('Escolha seu caminho:\n[1] - Caminho Vermelho\n[2] - Caminho Preto\n')) # 1
    if sala == 10:
        sala = randint(1, 5)
        print('OPAAAA! Você entrou em um portal controlado por criaturas místicas e elas controlam todo o '
              'tempo-espaço.\nSua sorte será testada e você será redirecionado para uma nova sala.\n'
              f'Sala sorteada: {sala}')
    elif sala == 6:
        print('Você só poderá entrar na sala 8.')
        sala = 8
    interacoes += 1
if sala == 9 and interacoes < 7:
    print('Parabéns! Vocês chegaram na sala 9.\nO objetivo de explorar a Dungeon e sobreviver foi concluído!')
else:
    print('Vocês não conseguiram explorar a Dungeon no tempo permitido. Game over!')
