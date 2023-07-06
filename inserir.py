import banco


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

print('Preencha o formulario.')
print()
name = input('Nome do jogo: ')
print()
nv = input('Nivel de Dificuldade: ')
print()
hr = input('Quantidade de horas que o jogo estima: ')
print()
total = input('Total de horas jogadas: ')

segundo(name, nv, hr, total)


