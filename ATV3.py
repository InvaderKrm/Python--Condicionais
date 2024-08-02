def verifica(palavra):
    palavra = palavra.lower()
    invertida = palavra[::-1]
    if palavra == invertida:
        return True
    else:
        return False

inserida = input('Vamos descobrir se uma palavra é um palíndromo?\nInsira a palavra desejada: ')

if verifica(inserida):
    print(f'A palavra "{inserida}" é um palíndromo!')
else:
    print(f'A palavra "{inserida}" não é um palíndromo!')