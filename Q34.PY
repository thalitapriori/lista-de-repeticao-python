number = int(input('Numero: '))
# numeros primos
if number > 1:
    print(f'Numero: {number}')
    for i in range(2, number):
        print(f'Valor de i: {i}')
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')