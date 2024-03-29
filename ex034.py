a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a + b < c or a + c < b or b + c < a:
    print('O triângulo não existe!')
else:
    print('O triângulo existe!')
print('--- FIM ---')
