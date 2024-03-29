nome = str(input('Digite seu nome completo: ')).strip().title().split()
print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[len(nome)-1]}')
# Na parte len(nome)- 1, esse menos 1 serve para ler a posição do último objeto da lista.
