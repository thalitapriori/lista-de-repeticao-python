#Q18/Q19 Faça um programa que, dado um conjunto de N números, determine o menor valor,
#o maior valor e a soma dos valores.

num = int(input('Digite um numero entre 0 e 1000: '))
maior = 1000
menor = 0

cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()

while cc not in 'N':
    num = int(input('Digite um numero: '))
    
    if num > maior:
        maior >= 1000
    if maior < menor:
        menor <= 0

    cc = str(input('Deseja continuar? S - Sim / N - Não  ')).upper()


print('O MAIOR número digitado foi {}.'.format(maior))
print('O MENOR número digitado foi {}.'.format(menor))