import os

lista = []
modo_op=input('Você deseja entrar no modo de operação? Digite [S] para sim e [N] para não.\n')
while True:
    if modo_op == 'S' or modo_op == 's':
        print('Você entrou no modo de Operação.')
        print('Selecione uma opção')
        opcao = input('[i] para inserir [a] para apagar [l] para listar: ')
    else:
        print('Você selecionou a opção "Não", Favor voltar para o menu.')
        break
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Digite um produto: ')
        lista.append(valor)
       # Colocar  a função do banco de dados para puxar a lista
    elif opcao == 'a':
        for i, valor in enumerate(lista):
            print(i, valor, sep=' - ')
        indice_str = input('Escolha o número do produto para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar este produto.')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Lista vazia')

        for i, valor in enumerate(lista):
            print(str(i+1), valor, sep=' - ')
    else:
        print('Opção inválida')