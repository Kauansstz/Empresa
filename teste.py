while True:
    entrada = input('Você quer "Entrar" ou "Sair"? [E] para entrar e [S] para sair: ' )   
    login = 'kauanss'
    login = 'Pedro'
    login = 'Lana'
    login = 'Cascao'
    login_permitido = login
    senha_permitida = 123
    # senha_digitada = int(senha_digitada)

 
    if (entrada == 'E' or entrada == 'e'): 
        login = input('Digite o seu Úsuario: ')
        senha_digitada = input('Senha: ')
        

        if login == login_permitido and senha_digitada == senha_permitida:
            print('Bem-Vindo!\nVocê entrou no sistema')
            input('Pesquisar: ')
            

        else:
            print('Login ou a senha incorreto!')
            break
 
    elif entrada == 'S' or entrada == 's':
        print('Você saiu do sistema') 
        break

    else:
        print('Você não digitou nem "entrar" e nem "sair"!')






