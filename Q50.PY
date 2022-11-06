def fatorial_for(numero):
    resultado = 1
    for k in range(1, numero + 1):
        resultado *= k
    return resultado

n = int(input('Digite um número inteiro positivo: '))
s = 1
soma = 0
string = "s = "
straux = ""
for i in range(1, n + 1):

    if i == 1:
        straux = straux + str(i)
    else:
        straux = straux + "1" + "/" + str(s)

    soma += (1/s)

    if i < n:
        straux = straux + " + "

    s = (s + 1)

print(string + straux)
print("H = " + str(soma))