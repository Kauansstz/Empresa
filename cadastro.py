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
    if (cadastro == 'S' or cadastro == 's'): 
        usuario = input('Úsuario: ')
        senha_digitada = input('Senha: ')
        email_digitado = input('Email: ')
        
    else:
        print('Redericionando para o menu.')
        break
    if usuario in login or email_digitado in email:
        print('Usuario já cadastrado.')

    else:
        print('Usuario não cadastrado.')
        cas = input('Deseja cadastrar? ')

        if cas == 's':
            login.append(usuario)
            senha_permitida.append(senha_digitada)
            email.append(email_digitado)
               
        
        else:
             print('Redericionando para o menu.')