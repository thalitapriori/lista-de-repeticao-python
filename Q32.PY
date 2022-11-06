numero = int(input("Fatorial de: ") )

if numero == 0:
    print(f"Não é possivel calular o fatorial do número {numero}")
    exit()

strResultado = str(numero) + '! = '
strResultadoAux = ''
resultado = 1
count = 1

for i in range(numero,0,-1):
    resultado *= count
    count += 1
    strResultadoAux += str(i)
    if i > 1:
        strResultadoAux += ' x '

print(strResultado + strResultadoAux + ' = ' +  str(resultado))