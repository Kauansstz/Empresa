import banco
import login

import tkinter as tk
from tkinter import Tk, Label, Button, Pack, Entry, PhotoImage, ttk
from PIL import ImageTk, Image



    
def tela():
    # Configuração Janela
    janela = Tk()
    janela.geometry('1024x768')
    janela.title("Lista")
    janela.iconbitmap("imagens/icone.ico")
    janela.config(background='white')
    # entrada = btn.get()
    # Configuração da Janela

    img = Image.open("C:/Users/V/Desktop/projeto/imagens/paisagem.jpg")
    img = img.resize((1600,980))
    img_tk = ImageTk.PhotoImage(img)
    img_label = Label(janela, image=img_tk)
    img_label.place(x=0, y=0)

    txt1 = Label(janela, text='Lista', font=('Arial',42, ), background='white')
    txt1.pack(padx=80, pady=80)

    txt2 = Label(janela, text='Login', font=('Arial',15), background='white')
    txt2.pack(padx=15, pady=10)

    caixa1 = Entry(janela, text="Login", font=('Arial',15))
    caixa1.pack(padx=12, pady=8)

    txt3 = Label(janela, text='Senha', font=('Arial',15), background='white')
    txt3.pack(padx=15, pady=10)

    caixa2 = Entry(janela, text="senha", font=('Arial',15), background='white')
    caixa2.pack(padx=12, pady=8)

    btn = Button(janela, text='Entrar', font=(16), background='#4798e8', fg='white', width=10)
    btn["command"] = lambda a=caixa1, b=caixa2: usuario(janela,a, b)
    btn.pack(padx=25, pady=30)
   
    lb = Label(janela, text="Esqueci a minha senha", font=('Arial black', 10), fg='blue')
    lb.config(bg=janela['bg'])
    lb.pack(padx=40, pady=45)
    # Configuração das Imagens
    imagem = Image.open("C:/Users/V/Desktop/projeto/imagens/cadeado.ico")
    imagem = imagem.resize((25, 25))  
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = Label(janela, image=imagem_tk)
    label_imagem.place(x=399, y=559)

    
    def usuario(janela1, a='', b=''):
        flag = False
       
        try:
            result = banco.sql_query(f"""SELECT count(*) FROM tabela_login WHERE login = '{a.get()}' and senha = '{b.get()}'""")
            if result[0][0] == 1:
                flag = True

        except:
             flag = True
        if flag:
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            user = Label(janela, text='Úsuario:' , font=('Arial',10))
            user.place(x=0, y=0)
            botao1 = Button(janela, text='Inserir', font=('Arial', 20), background='white', width= 20)
            botao1["command"] = lambda botao1=botao1: inserir(janela)
            botao1.place(x=300, y=200)
            botao2 = Button(janela, text='Consultar', font=('Arial', 20), background='white', width= 20)
            botao2["command"] = lambda botao2=botao2: con(botao2, janela)
            botao2.place(x=300, y=300)
            botao3 = Button(janela, text='Deletar', font=('Arial', 20), background='white', width= 20)
            botao3["command"] = lambda botao3=botao3: apagar( janela)
            botao3.place(x=300, y=400)

            
        else:
            mensagem = Label(janela, text="Login ou senha está incorreto!", font=('Arial black', 10), fg = 'red')
            mensagem.place(x= 400, y=530)
            
    

        def con(botao2,janela):
            result = banco.sql_query('select * from listas_tabelas_jogos')
            
            if len(result) > 0:
                janela.destroy()
                janela = Tk()
                janela.geometry('1024x768')
                janela.title("Lista")
                janela.iconbitmap("imagens/icone.ico")
                janela.config(background='white')
                table = ttk.Treeview(janela, selectmode="extended", columns=("col1", "col2", "col3", "col4"))
                table.grid(row=0, column=0, sticky="nsew")
                table.heading("col1", text="Quantidade de horas")
                table.heading("col2", text="Nome do jogo")
                table.heading("col3", text="Total de Horas")
                table.heading("col4", text="Nivel da Dificuldade")
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
            else:
                print('foda')

        def delete(name):
                banco.sql_inserir(f"""DELETE FROM listas_tabelas_jogos WHERE nome_jogo = '{name}'""")
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
        def delete(name):
                banco.sql_inserir(f"""DELETE FROM listas_tabelas_jogos WHERE nome_jogo = '{name}'""")
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

        def insercao(nj,df,qh,th):
            banco.sql_inserir(f"""INSERT INTO listas_tabelas_jogos
                                (nome_jogo, 
                                nv_dificuldade, 
                                quantidade_de_horas, 
                                total_horas) 
                                VALUES('{nj}'
                                        ,'{df}', 
                                        {qh},
                                        {th} )""")
        def inserir(janela1):
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            cx = Label(janela, text='Preencha o Formulario.', font=('Arial', 30), background='white')
            cx.pack(padx= 40, pady= 50)
            cx_txt1 = Label(janela, text=' - Nome do Jogo.',font=('Arial', 18), background='white')
            cx_txt1.place(x=10, y= 150)
            ent1 = Entry(janela, width=20, font=('Arial', 16), background='gray')
            ent1.place(x=10, y=180)
            cx_txt2 = Label(janela, text=' - Nivel do Jogo.',font=('Arial', 18), background='white')
            cx_txt2.place(x=10, y=240)
            ent2 = Entry(janela, width=20, font=('Arial', 16), background='gray')
            ent2.place(x=10, y=270)
            cx_txt3 = Label(janela, text=' - Horas que o jogo propoem.',font=('Arial', 18), background='white')
            cx_txt3.place(x=50, y= 150)
            ent3 = Entry(janela, width=20, font=('Arial', 16), background='gray')
            ent3.place(x=50, y=180)
            cx_txt4 = Label(janela, text=' - Total de Horas jogadas.',font=('Arial', 18), background='white')
            cx_txt4.place(x=100, y=180)
            ent4 = Entry(janela, width=20, font=('Arial', 16), background='gray')
            ent4.place(x=100, y=180)
            botao6 = Button(janela, text='Executar',width=20, background='blue', font=('Arial', 16), fg ='white' )
            botao6.place(x=450, y=500)
    janela.mainloop()
   
tela()