n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if n1 > n2 > n3:
    print(f'{n1} é o maior e {n3} é o menor!')
elif n1 > n3 > n2:
    print(f'{n1} é o maior e {n2} é o menor!')
elif n2 > n1 > n3:
    print(f'{n2} é o maior e {n3} é o menor!')
elif n2 > n3 > n1:
    print(f'{n2} é o maior e {n1} é o menor!')
elif n3 > n1 > n2:
    print(f'{n3} é o maior e {n2} é o menor!')
else:
    print(f'{n3} é o maior e {n1} é o menor!')
print('--- FIM ---')
