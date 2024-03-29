sal = float(input('Salário do funcionário: '))
if sal <= 1250.00:
    aumento = sal * 15/100
    print(f'O aumento será de R${aumento:.2f}.')
else:
    aumento = sal * 10/100
    print(f'O aumento será de R${aumento:.2f}.')
print('--- FIM ---')
