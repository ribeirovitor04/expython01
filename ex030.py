dist = float(input('Distância da viagem (em km): '))
if dist <= 200:
    print(f'O preço da passagem será de R${dist*0.50}.')
else:
    print(f'O preço da passagem será de R${dist*0.45}.')
print('--- FIM ---')
