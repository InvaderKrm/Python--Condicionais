numero = int(input('Descubra a tabuada de um número com Python!\nDigite o número desejado: '))
for i in range (10):
    conta = numero*(i+1)
    print(f'{numero} x {i+1} = {conta}')