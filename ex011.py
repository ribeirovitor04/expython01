l = float(input('Largura da parede (em metros): '))
h = float(input('Altura da parede (em metros): '))
a = l*h
tinta = a/2
print(f'A parede possui dimensões {l} x {h} e possui {a:.2f}m² de área.\nA quantidade de tinta necessária para pintar a parede é de {tinta:.2f}L de tinta.')
