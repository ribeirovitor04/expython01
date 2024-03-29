frase = str(input('Digite um frase: ')).strip().casefold()
print(f'A letra A aparece {frase.count('a')} vezes.')
print(f'A primeira letra A apareceu na {frase.find('a')+1}° posição.')
print(f'A última letra A apareceu na {frase.rfind('a')+1}° posição.')
