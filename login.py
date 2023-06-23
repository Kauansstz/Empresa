import os


entrada = input('Você quer "Entrar" ou "Sair"? [E] para entrar e [S] para sair: ' )   
login = 'kauanss'
login_permitido = login

senha_permitida = '123'

while True:
    if (entrada == 'E' or entrada == 'e'): 
        login = input('Digite o seu Úsuario: ')
        senha_digitada = input('Senha: ')
        

        if login == login_permitido and senha_digitada == senha_permitida:
            print('Bem-Vindo!\nVocê entrou no sistema')
            os.system('cls')
            
        else:
            print('Login ou a senha incorreto!')
            break
 
    else:
        print('Você saiu do sistema') 
        break