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
    straux = straux + str(i) + "/" + str(s)

    soma += (i/s)

    if i < n:
        straux = straux + " + "

    s = (s + 2)

print(string + straux)
print("Soma: " + str(soma))