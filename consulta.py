import banco

def main():
    result=   banco.sql_query('select * from listas_tabelas_jogos')
    print(result)
    




main()