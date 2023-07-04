import banco

def apagar(name):
   banco.sql_inserir (f"""DELETE FROM listas_tabelas_jogos WHERE nome_jogo = '{name}'""" )
name = input('Nome do jogo: ')
print()
print('Itens apagados são:\n',name)
apagar(name)

