nome = input('Digite seu nome completo: ')
a = nome.split()
b = ''.join(a)
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.casefold()}')
# Ou no lugar de CASEFOLD poderia ser colocado LOWER
print(f'Seu nome completo tem {len(b)} letras.')
print(f'Seu primeiro nome é {a[0]} e ela tem {len(a[0])} letras.')

#nome = str(input('Digite seu nome completo: ')).strip()
#print(f'Seu nome em maiúsculas é {nome.upper()}')
#print(f'Seu nome em minúsculas é {nome.casefold()}')
#print(f'Seu nome completo tem {len(nome)-nome.count(' ')} letras.')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras.')
