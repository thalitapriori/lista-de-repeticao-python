#Q03 Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

def input_nome():
    valida_nome = False
    nome = str(input('Digite nome: ')).strip().upper()
    while not valida_nome:
        if len(nome) < 3:
            print('Dados inválidos, seu nome precisa ter no minímo 3 caracteres!')
            nome = str(input('Digite nome: ')).strip().upper()
        else:
            valida_nome = True

def input_idade():
    valida_idade = False
    idade = int(input('Digite idade: '))
    while not valida_idade:
        if idade < 1 or idade > 150:
            print('Dados invalidos!')
            idade = int(input('Digite idade: '))
        else:
            valida_idade = True

def input_salario():
    salario = float(input('Digite salario: '))
    while salario < 1:
        print('Dados invalidos!')
        salario = float(input('Digite salario: '))

def input_sexo():
    valida_sexo = False

    while not valida_sexo:
        sexo = str(input('Digite sexo: [M ou F] ')).upper().strip()
        if len(sexo) > 1 or sexo not in 'MF':
            print('Dados invalidos')
        else:
            valida_sexo = True

def input_estado_civil():
    valida_estado_civil = False
    while not valida_estado_civil:
        estado_civil = str(input('Estado civil:\n[S] Solteiro\n[C] Casado\n[V] Viuvo\n[D] Dirvociado\n')).upper().strip()
        if len(estado_civil) > 1 or estado_civil not in 'SCV':
            print('Dados invalidos!')
        else:
            valida_estado_civil = True

input_nome()
input_idade()
input_sexo()
input_estado_civil()
input_salario()