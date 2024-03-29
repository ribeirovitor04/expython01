vel = int(input('Velocidade do carro (em km/h): '))
if vel <= 80:
    print('Dentro da velocidade!')
else:
    excesso = vel - 80
    multa = excesso * 7
    print(f'MULTADO!\nExcesso de {excesso} km/h!\nMulta de R${multa:.2f}.')
print('--- FIM ---')
