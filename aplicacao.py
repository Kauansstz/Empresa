import banco

import tkinter as tk
from tkinter import Tk, Label, Button, Entry, ttk, messagebox




    
def tela():
    # Configuração Janela
    janela = Tk()
    janela.geometry('1024x768')
    janela.title("Lista")
    janela.iconbitmap("imagens/icone.ico")
    janela.config(background='white')
    
    txt1 = Label(janela, text='Lista', font=('Arial',42, ), background='white')
    txt1.pack(padx=80, pady=80)

    txt2 = Label(janela, text='Login', font=('Arial',15), background='white')
    txt2.pack(padx=15, pady=10)

    caixa1 = Entry(janela, text="Login", font=('Arial',15))
    caixa1.pack(padx=12, pady=8)

    txt3 = Label(janela, text='Senha', font=('Arial',15), background='white')
    txt3.pack(padx=15, pady=10)

    caixa2 = Entry(janela, text="senha", font=('Arial',15), background='white', show='*')
    
    caixa2.pack(padx=12, pady=8)

    btn = Button(janela, text='Entrar', font=(16), background='blue', fg='white', width=10)
    btn["command"] = lambda a=caixa1, b=caixa2: usuario(janela,a, b)
    btn.pack(padx=25, pady=30)
   
    lb = Label(janela, text="Esqueci a minha senha", font=('Arial black', 10), fg='blue')
    lb.config(bg=janela['bg'])
    lb.pack(padx=40, pady=45)
    

    
    def usuario(janela1, a='', b=''):
        flag = False
       
        try:
            result = banco.sql_query(f"""SELECT count(*) FROM tb_login WHERE login = '{a.get()}' and senha = '{b.get()}'""")
            if result[0][0] == 1:
                flag = True
                
            else:
                messagebox.showerror("Error!", "Login ou Senha incorreto!")

        except:
             flag = True
        if flag:
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Menu Principal")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            user = Label(janela, text='Úsuario:' , font=('Arial',10))
            user.place(x=0, y=0)
            bnt = Button(janela, text='Criar Tabela', font=('Arial', 20), background='white', width=20 )
            bnt ["command"]= lambda bnt=bnt: create_table(janela)
            bnt.pack(padx= 10, pady=20)
            botao1 = Button(janela, text='Inserir', font=('Arial', 20), background='white', width= 20)
            botao1["command"] = lambda botao1=botao1: inserir(janela)
            botao1.pack(padx=10, pady=20)
            botao2 = Button(janela, text='Consultar', font=('Arial', 20), background='white', width= 20)
            botao2["command"] = lambda botao2=botao2: con(botao2, janela)
            botao2.pack(padx=10, pady=20)
            botao3 = Button(janela, text='Deletar', font=('Arial', 20), background='white', width= 20)
            botao3["command"] = lambda botao3=botao3: apagar( janela)
            botao3.pack(padx=10, pady=20)

        def con(botao2,janela):
            result = banco.sql_query('select * from list_jogos')
            
            if len(result) > 0:
                janela.destroy()
                janela = Tk()
                janela.geometry('1024x768')
                janela.title("Lista")
                janela.iconbitmap("imagens/icone.ico")
                janela.config(background='white')
                table = ttk.Treeview(janela, selectmode="extended", columns=("col1", "col2", "col3", "col4"))
                table.grid(row=0, column=0, sticky="nsew")
                table.heading("col1", text="Nome do Jogo")
                table.heading("col2", text="Dificuldade")
                table.heading("col3", text="Horas jogadas")
                table.heading("col4", text="Total de Horas")
                table.column("#0", width=0, stretch=tk.NO)
                table.column("col1", width=450)
                table.column("col2", width=140)
                table.column("col3", width=100)
                table.column("col4", width=100)
                for i in result:
                    table.insert("", "end", values=(i[0], i[1], i[2], i[3]))
                    print(i)
                scrollbar = ttk.Scrollbar(janela, orient="vertical", command="table.yview")
                scrollbar.grid(row=0, column=1, sticky="ns")
                table.configure(yscrollcommand=scrollbar.set)
                janela.grid_rowconfigure(0, weight=1)
                janela.grid_columnconfigure(0, weight=1)
                botao8= Button(janela, text="Voltar", background='blue', fg='white', font=('Arial', 18), width=10)
                botao8["command"]= lambda botao8=botao8: usuario(janela)
                botao8.place(x=500, y= 500)              
            else:
                print('foda')

        def delete(name):
                banco.sql_inserir(f"""DELETE FROM list_jogos WHERE nome_jogo = '{name}'""")
                return 'Deletado com sucesso'
        
        def apagar( janela1):
            
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            txt = Label(janela, text=' Digite o nome do jogo para apagar.',font=('Arial', 18), background='white')
            txt.place(x=290,y=200)
            caixa_txt = Entry(janela,width=28 ,font=('Arial',18))
            caixa_txt.place(x=304, y=300)

            botao4= Button(janela,text="Executar",font=('Arial',18), background='blue', fg='white', width=10)
            botao4["command"] = lambda name=caixa_txt: delete(name.get())
            botao4.place(x= 500, y= 400)
            botao5= Button(janela,text="Voltar",font=('Arial',18), background='blue', fg='white', width=10)
            botao5["command"] = lambda botao5=botao5: usuario(janela)
            botao5.place(x= 320, y= 400)
        
        def incluir(nj,df,qh,th):
           banco.sql_inserir(f"""INSERT INTO list_jogos
                        ( NOME_JOGO,
                        DIFICULDADE,
                        QTN_HORAS,
                        TOTAL_HORAS) 
                         VALUES('{nj}'
                                ,'{df}', 
                                {qh},
                                {th} )""")
           return 'Deu certo'

        def inserir(janela1):
            #configurações da janela
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            #configurações da janela
            #configurações dos botões e Frases
            cx = Label(janela, text='Preencha o Formulario.', font=('Arial', 30), background='white')
            cx.pack(padx= 40, pady= 50)
            cx_txt1 = Label(janela, text='Nome do Jogo.',font=('Arial', 18), background='white', )
            cx_txt1.place(x=250, y= 150)
            ent1 = Entry(janela, width=22, font=('Arial', 16), background='gray', fg='white')
            ent1.place(x=250, y=190)
            cx_txt2 = Label(janela, text='Nivel do Jogo.',font=('Arial', 18), background='white')
            cx_txt2.place(x=250, y=240)
            ent2 = Entry(janela, width=22, font=('Arial', 16), background='gray', fg='white')
            ent2.place(x=250, y=270)
            cx_txt3 = Label(janela, text=' Horas de jogo.',font=('Arial', 18), background='white')
            cx_txt3.place(x=600, y= 150)
            ent3 = Entry(janela, width=22, font=('Arial', 16), background='gray', fg='white')
            ent3.place(x=600, y=190)
            cx_txt4 = Label(janela, text='Total de Horas jogadas.',font=('Arial', 18), background='white')
            cx_txt4.place(x=600, y=240)
            ent4 = Entry(janela, width=22, font=('Arial', 16), background='gray', fg='white')
            ent4.place(x=600, y=270)
            botao6 = Button(janela, text='Executar',width=15, background='blue', font=('Arial', 16), fg ='white' )
            botao6["command"] = lambda nj=ent1, df=ent2, qh=ent3, th= ent4: incluir(nj.get(),df.get(), qh.get(),th.get())
            botao6.place(x=550, y=400)
            botao7 = Button(janela, text='Voltar', width=15, background='blue', font=('Arial', 16), fg='white')
            botao7["command"] = lambda botao7=botao7: usuario(janela)
            botao7.place(x=300, y=400)
            #configurações dos botões e Frases
            
        def create_table(janela1):
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            l_txt = Label(janela, text='Nome do formulário que deseja criar.',font=('Arial', 18), background='white')
            l_txt.pack(padx=40, pady= 100)
            ent1 = Entry(janela, width=22, font=('Arial', 16), background='white')
            ent1.pack(padx=0, pady=0)
            bnt_next = Button(janela, width=22, font=('Arial', 16), background='blue', fg='white',text='Avançar')
            bnt_next["command"] = lambda bnt_next=bnt_next:create_table_info(janela)
            bnt_next.pack(padx=10, pady=100)
            
        def create_table_info(janela1):
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            l_txt = Label(janela, text='Qual o estilo do formulário?',font=('Arial', 18), background='white')
            l_txt.pack(padx=100, pady=100)
            bnt_list = Button(janela, text="Lista",width=22, font=('Arial', 16), background='blue', fg='white')
            bnt_list.pack(padx=50, pady=20 )
            bnt_table=Button(janela, text="Tabela",width=22, font=('Arial', 16), background='blue', fg='white')
            bnt_table.pack(padx=50, pady=20 )
    janela.mainloop()
   
tela()