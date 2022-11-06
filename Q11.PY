#Q11-Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input('Infomer um numero inteiro: '))
n2 = int(input('Infomer outro numero inteiro: '))
soma = 0
if n1 > n2:
    for a in range(n2+1,n1):
        print(a)
        soma = soma + a

elif n1 < n2:
    for a in range(n1+1,n2):
        print(a)
        soma = soma + a
else:
    print('Os numeros são iguais.')
print(f'A soma dos numeros foi de {soma}')
