import banco

def main():
    result = banco.sql_query('select * from listas_tabelas_jogos')
    for i in result:
            dict = {}
            dict['nome_jogo'] = i[1]
            dict['quantidade_de_horas'] = i[0]
            dict['nv_dificuldade'] = i[3]
            print(dict)




main()