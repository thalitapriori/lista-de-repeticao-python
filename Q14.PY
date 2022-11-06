impar = 0
par = 0
numeros = 10
for a in range (1,11):
        valor = input(f"Informe o {a}º numero interiro: ")
        while not valor.isdigit():
            valor = input(f"Informe o {a}º numero interiro: ")
        while  valor.isdigit():
            valor = int(valor)
            if (valor % 2) == 0:
                par = par + 1
                valor = str(valor)
                break
            else:
                impar = impar + 1
                valor = str(valor)
                break
print(f'A quantidade de numeros impar(es) foi {impar} e numeros par(es) foi {par}.')