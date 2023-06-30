# Perguntar ao tipo de usuario que tipo de lista dever ser criado
# Pessoal, empresa, compras, video game, receita....

criar = input('Você deseja criar uma lista ?\n')

while True:

    if criar ==  'Sim' or criar == 'sim':
        opcao = input(
            'Qual o propósito da criação?\nPessoal[P]\nEmpresarial[E]\nAnotar Receitas[AE]\n'
            )
        print()
        #aparecer uma imagem correspondente com a opção 
        if opcao == 'P' or opcao == 'p':
            
            print('Criado') #redenrecionar para a lista

        if opcao == 'E' or opcao == 'e':
            print('Criado') #redenrecionar para a lista

        if opcao == 'ae' or opcao == 'AE':
            print('Criado') #redenrecionar para a lista
         
        else:
            print('Rederecionando para a lista')
        break
    else:
        print('Rederecionando para a lista')
        break