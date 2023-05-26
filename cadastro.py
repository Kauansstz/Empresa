'''
Aba para o Usuario fazer o cadastro.
Requisitos: nickname, email e senha.
'''

import os


cadastro = input('Deseja fazer login?\n' )   
login = ['a']
senha_permitida = ['123']
email = ['bb']

while True:
    if (cadastro == 'Sim' or cadastro == 'sim'): 
        usuario = input('Úsuario: ')
        senha_digitada = input('Senha: ')
        email_digitado = input('Email: ')
        
    elif cadastro == 'não' or cadastro == 'Não':
        print('Redericionando para o login.')
    
    else:
        print('Você não digitou sim ou não.')
        break
    if usuario in login or email_digitado in email:
        print('Usuario já cadastrado.')

    else:
        print('Usuario não cadastrado.')
        cas = input('Deseja cadastrar? ')

        if cas == 's' or cas == 'S':
            print('Preencha os campos necessarios para realizar o cadastro')
            print()
            login_nv = input('Insira o usuario: ')
            senha_nv = input('Insira a senha: ')
            email_nv = input('Insira a email: ')
            login.append(usuario)
            senha_permitida.append(senha_digitada)
            email.append(email_digitado)
            print('Login criado, Redericionando para o menu')
        
        else:
             print('Redericionando para o login.')