import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O ângulo digitado foi {ang}.\nO seno do ângulo é {sen:.2f}.\nO cosseno do ângulo é {cos:.2f}.\nA tangente do ângulo é {tg:.2f}.')

# É necessário transformar a variável ANG emradianos para as funções sin, cos e tan ler!
