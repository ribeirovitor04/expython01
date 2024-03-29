import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'O nome escolhido foi {escolhido}.')

# O código choice escolhe UM item dentro da lista!
