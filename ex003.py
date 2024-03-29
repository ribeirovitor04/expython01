n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
cores = {'limpa' : '\033[m',
         'verde' : '\033[4;32m'}
print(f'A soma de {cores["verde"]}{n1}{cores["limpa"]} e {cores["verde"]}{n2}{cores["limpa"]} é igual a {cores["verde"]}{soma}{cores["limpa"]}!')
# print(f'A soma de {n1} e {n2} é igual a {soma}!')
