a = input('Digite algo: ')
cores = {'limpa': '\033[m',
         'verde': '\033[4;32m'}
print(f'O tipo primitivo desse valor é {cores["verde"]}{type(a)}{cores["limpa"]}.')
print(f'Só tem espaços? {cores["verde"]}{a.isspace()}{cores["limpa"]}.')
print(f'É um número? {cores["verde"]}{a.isnumeric()}{cores["limpa"]}.')
print(f'É alfabético? {cores["verde"]}{a.isalpha()}{cores["limpa"]}.')
print(f'É alfanumérico? {cores["verde"]}{a.isalnum()}{cores["limpa"]}.')
print(f'Está em maiúsculas? {cores["verde"]}{a.isupper()}{cores["limpa"]}.')
print(f'Está em minúsculas? {cores["verde"]}{a.islower()}{cores["limpa"]}.')
print(f'Está capitalizada? {cores["verde"]}{a.istitle()}{cores["limpa"]}.')
