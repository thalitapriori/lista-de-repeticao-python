#Q02-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando 
#a pedir as informações.

usuario =  input ("Digite seu usuario: ")
senha = input( "Digite sua senha: ")

while  usuario == senha :
	print ( "ERRO: o usuário não pode ser igual a senha tente novamente" )
	usuario = str ( input ( "Digite seu usuario: " ))
	senha = int(input( "Digite Nova Senha: " ))
	print ("Cadastrado realizado com sucesso!!" )

