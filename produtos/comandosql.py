import banco

def main():
    result = banco.sql_query('select * from listas_tabelas_jogos')
    for i in result:
            dict = {}
            dict['quantidade_de_horas'] = i[0]
            dict['nome_jogo'] = i[1]
            dict['nv_dificuldade'] = i[3]
            print(dict)

#main()

def segundo(nj,df,qh,th):
      banco.sql_inserir(f"""INSERT INTO listas_tabelas_jogos
                        (nome_jogo, 
                         nv_dificuldade, 
                         quantidade_de_horas, 
                         total_horas) 
                         VALUES('{nj}'
                                ,'{df}', 
                                {qh},
                                {th} )""")

#segundo('cuphead', 'extremo', 90, 140)

main()