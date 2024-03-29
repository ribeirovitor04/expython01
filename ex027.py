from random import randint
from time import sleep
print('-=-' * 20)
print('Pensei em um número entre 0 e 5, consegue adivinhar qual é?')
print('-=-' * 20)
comp = randint(0, 5)
# Deixa os números aleatórios!
num = int(input('Tente a sorte aqui e digite um número: '))
print('PROCESSANDO...')
sleep(2)
# Dá um delay (em segundos) para o programa rodar!
if num == comp:
    print('Parabéns, você acertou o número!')
else:
    print(f'Você perdeu! Eu pensei no número {comp}, não em {num}.')
print('--- FIM ---')
