while True:
    entrada = input('Você quer "Entrar" ou "Sair"? [E] para entrar e [S] para sair: ' )
    senha_digitada = input('Senha: ')
    senha_permitida = 123456
    senha_digitada = int(senha_digitada)

 
    if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida: 
         print('Bem - Vindo!\nVoce entrou no sistgema')
         
         break
 
    elif entrada == 'S':
        print('Você saiu do sistema') 
        break

    else:
        print('Você não digitou nem entrar e nem sair')

pesquisar = input('Você deseja pesquisar algo? [Y] para sim e [N] para não: ')

if pesquisar == 'Y' or pesquisar == 'y':
   input('Dígite o que deseja pesquisar:\n'),

elif  pesquisar == 'N' or pesquisar == 'n':...




