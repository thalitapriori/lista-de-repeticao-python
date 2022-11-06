def eh_primo(number):
    eh_primo = False
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            eh_primo = True
    return eh_primo

numero = int(input("\nDigite um número: "))
lista = []

for i in range(1, numero + 1):
    if eh_primo(i):
        lista.append(i)

print("Números primos: ", lista)