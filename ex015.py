dias = int(input('Dias alugados: '))
km = float(input('Km percorridos: '))
total = 60*dias+0.15*km
print(f'O preço que deverá ser pago será de {total:.2f} reais.')
