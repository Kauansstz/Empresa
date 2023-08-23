import banco
import cx_Oracle
import re
import tkinter as tk
from tkinter import Tk, Label, Button, Entry, ttk, messagebox






def screen():
    # Configuração Janela
    # Initial screen, this screen will collect the user's login and password and check if you have a login registered in the database, if you don't have it, if you don't have it, 
    # you have to contact the adm, if the login or password is incorrect , an error message will appear.
    Windows = Tk()
    Windows.geometry('1024x768')
    Windows.title("Lista")
    Windows.iconbitmap("imagens/icone.ico")
    Windows.config(background='white')
    
    text_box_tittle = Label(Windows, text='Lista', font=('Arial',42, ), background='white')
    text_box_tittle.pack(padx=80, pady=80)

    text_box_logout = Label(Windows, text='Login', font=('Arial',15), background='white')
    text_box_logout.pack(padx=15, pady=10)

    inbox_user = Entry(Windows, text="Login", font=('Arial',15), background='white')
    inbox_user.pack(padx=12, pady=8)

    text_box_password = Label(Windows, text='Senha', font=('Arial',15), background='white')
    text_box_password.pack(padx=15, pady=10)

    inbox_password = Entry(Windows, text="senha", font=('Arial',15), background='white', show='*')
    inbox_password.pack(padx=12, pady=8)

    enter_button = Button(Windows, text='Entrar', font=(16), background='blue', fg='white', width=10)
    enter_button["command"] = lambda login=inbox_user, password=inbox_password: menu(Windows,login, password)
    enter_button.pack(padx=25, pady=30)

    
    
    def menu(Windows1, login = '', password =''):
        #After logging in, you will go to the menu screen where there are 4 buttons, 
        # where you have the button to insert, delete and consult the data and the fourth button, which serves to create tables
        flag= False
        
        try:
            result = banco.sql_query(f"""SELECT count(*) FROM tb_login WHERE login = '{login.get().upper()}' and senha = '{password.get().upper()}'""")
            if result[0][0] == 1:
                flag = True
        except:
            flag = True
        if flag:
            Windows1.destroy()
            Windows = Tk()
            Windows.geometry('1024x768')
            Windows.title("Menu Principal")
            Windows.iconbitmap("imagens/icone.ico")
            Windows.config(background='white')
            button_create = Button(Windows, text='Criar Tabela', font=('Arial', 20), background='white', width=20 )
            button_create ["command"]= lambda bnt=button_create: create_table_info(Windows)
            button_create.pack(padx= 10, pady=50)
            button_insert = Button(Windows, text='Inserir', font=('Arial', 20), background='white', width= 20)
            button_insert["command"] = lambda botao1=button_insert: insert(Windows)
            button_insert.pack(padx=10, pady=50)
            button_query = Button(Windows, text='Consultar', font=('Arial', 20), background='white', width= 20)
            button_query["command"] = lambda botao2=button_query: consult_info( Windows)
            button_query.pack(padx=10, pady=50)
            button_delete  = Button(Windows, text='Deletar', font=('Arial', 20), background='white', width= 20)
            button_delete ["command"] = lambda botao3=button_delete : delete_info(Windows)
            button_delete .pack(padx=10, pady=50)
        else:
            text_box_error = Label( text='Não possui cadastro? Favor entrar em contato com o administrador.', font=('Arial',15), background='white')
            text_box_error.pack(padx=15, pady=10)
            messagebox.showerror("Error!", "Login ou Senha incorreto!")


            
        def consult_info(Windows1 ):
            # search the database if the table exists and will return with the data
            result = banco.sql_query(f"""SELECT * FROM list_jogos """)
            
            if len(result[0][0]) > 1:
                    Windows1.destroy()
                    Windows = Tk()
                    Windows.geometry('1024x768')
                    Windows.title("Lista")
                    Windows.iconbitmap("imagens/icone.ico")
                    Windows.config(background='white')
                    table = ttk.Treeview(Windows, selectmode="extended", columns=("col1", "col2", "col3", "col4"))
                    table.grid(row=0, column=0, sticky="nsew")
                    table.heading("col1", text="coluna1" )
                    table.heading("col2", text="coluna2")
                    table.heading("col3", text="coluna3")
                    table.heading("col4", text="coluna4")
                    table.column("#0", width=0, stretch=tk.NO)
                    table.column("col1", width=450)
                    table.column("col2", width=140)
                    table.column("col3", width=100)
                    table.column("col4", width=100)
                    for i in result:
                        table.insert("", "end", values=(i[0], i[1], i[2], i[3]))
                        print(i)
                    scrollbar = ttk.Scrollbar(Windows, orient="vertical", command="table.yview")
                    scrollbar.grid(row=0, column=1, sticky="ns")
                    table.configure(yscrollcommand=scrollbar.set)
                    Windows.grid_rowconfigure(0, weight=1)
                    Windows.grid_columnconfigure(0, weight=1)
                    button_back= Button(Windows, text="Voltar", background='blue', fg='white', font=('Arial', 18), width=10)
                    button_back["command"]= lambda botao8=button_back: menu(Windows)
                    button_back.place(x=500, y= 500)   
            else:
                messagebox.showerror("Erro!", "Tabela inexistente")
            return result          
        def delete(name):
                banco.sql_inserir(f"""DELETE FROM list_jogos WHERE nome_jogo = '{name}'""")
                return 'Deletado com sucesso'
        
        def delete_info( Windows1):
            # The function will collect column name and directly delete in database
            Windows1.destroy()
            Windows = Tk()
            Windows.geometry('1024x768')
            Windows.title("Lista")
            Windows.iconbitmap("imagens/icone.ico")
            Windows.config(background='white')
            txt = Label(Windows, text=' Digite o nome da primeira coluna para deletar.',font=('Arial', 18), background='white')
            txt.place(x=290,y=200)
            caixa_txt = Entry(Windows,width=28 ,font=('Arial',18))
            caixa_txt.place(x=304, y=300)

            botao4= Button(Windows,text="Executar",font=('Arial',18), background='blue', fg='white', width=10)
            botao4["command"] = lambda name=caixa_txt: delete(name.get())
            botao4.place(x= 500, y= 400)
            botao5= Button(Windows,text="Voltar",font=('Arial',18), background='blue', fg='white', width=10)
            botao5["command"] = lambda botao5=botao5: menu(Windows)
            botao5.place(x= 320, y= 400)
        
        def enter(name_game, level, game_hours, total_hours):
            try:
                banco.sql_inserir(f"""INSERT INTO list_jogos
                                ( NOME_JOGO,
                                DIFICULDADE,
                                QTN_HORAS,
                                TOTAL_HORAS) 
                                VALUES('{name_game}'
                                        ,'{level}', 
                                        {game_hours},
                                        {total_hours} )""")
            except cx_Oracle.DatabaseError as e :
                error, = e.args
                messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro no banco de dados:\n{error.message}")
            return 'Deu certo'
        # Inserting information in the insert function and sending it to the enter function and including data in the table
        def insert(Windows1):
            #configurações da janela
            Windows1.destroy()
            Windows = Tk()
            Windows.geometry('1024x768')
            Windows.title("Lista")
            Windows.iconbitmap("imagens/icone.ico")
            Windows.config(background='white')
            box_form_text  = Label(Windows, text='Preencha o Formulario.', font=('Arial', 30), background='white')
            box_form_text .pack(padx= 40, pady= 50)
            box_text_name_game = Label(Windows, text='Nome do Jogo.',font=('Arial', 18), background='white', )
            box_text_name_game.place(x=250, y= 150)
            inbox_name_game = Entry(Windows, width=22, font=('Arial', 16), background='gray', fg='white')
            inbox_name_game.place(x=250, y=190)
            box_text_level = Label(Windows, text='Nivel do Jogo.',font=('Arial', 18), background='white')
            box_text_level.place(x=250, y=240)
            inbox_level = Entry(Windows, width=22, font=('Arial', 16), background='gray', fg='white')
            inbox_level.place(x=250, y=270)
            game_hours_text_box = Label(Windows, text=' Horas de jogo.',font=('Arial', 18), background='white')
            game_hours_text_box.place(x=600, y= 150)
            game_hours_inbox = Entry(Windows, width=22, font=('Arial', 16), background='gray', fg='white')
            game_hours_inbox.place(x=600, y=190)
            total_hours_played_txt_box = Label(Windows, text='Total de Horas jogadas.',font=('Arial', 18), background='white')
            total_hours_played_txt_box.place(x=600, y=240)
            total_hours_played_inbox = Entry(Windows, width=22, font=('Arial', 16), background='gray', fg='white')
            total_hours_played_inbox.place(x=600, y=270)
            execute_button = Button(Windows, text='Executar',width=15, background='blue', font=('Arial', 16), fg ='white' )
            execute_button["command"] = lambda name_game=inbox_name_game, level=inbox_level, game_hours=game_hours_inbox, total_hours= total_hours_played_inbox: enter(name_game.get(),
                                                                                                                                                                       level.get(), 
                                                                                                                                                                       game_hours.get(),
                                                                                                                                                                       total_hours.get())
            execute_button.place(x=550, y=400)
            butoon_back = Button(Windows, text='Voltar', width=15, background='blue', font=('Arial', 16), fg='white')
            butoon_back["command"] = lambda botao7=butoon_back: menu(Windows)
            butoon_back.place(x=300, y=400)
            
            
        def create_table(text_box_name, column1, column2, column3, column4 ):
            # Function creating a new table and pulling the information in the create_table_info function
            try:
                    table_name = text_box_name.get()
                    columns_text1 = column1.get()
                    columns_text2 = column2.get()
                    columns_text3 = column3.get()
                    columns_text4 = column4.get()
                    columns1 = [col1.strip() for col1 in re.split(r'[,\s]+', columns_text1)]
                    columns2 = [col2.strip() for col2 in re.split(r'[,\s]+', columns_text2)] 
                    columns3 = [col3.strip() for col3 in re.split(r'[,\s]+', columns_text3)] 
                    columns4 = [col4.strip() for col4 in re.split(r'[,\s]+', columns_text4)] 
                    column_1 = ', '.join([f'{col1.strip()} VARCHAR2(100)' for col1 in columns1])
                    column_2 = ', '.join([f'{col2.strip()} VARCHAR2(100)' for col2 in columns2])
                    column_3 = ', '.join([f'{col3.strip()} VARCHAR2(100)' for col3 in columns3])
                    column_4 = ', '.join([f'{col4.strip()} VARCHAR2(100)' for col4 in columns4])
                    # Chamada à função para inserir no banco
                    banco.sql_inserir(f"""CREATE TABLE {table_name} ({column_1},
                                                                      {column_2},
                                                                      {column_3},
                                                                      {column_4})""")
                    messagebox.showinfo("Informação", "Tabela Criada!")
            
            except cx_Oracle.DatabaseError as e :
                error, = e.args
                messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro no banco de dados:\n{error.message}")

        
            
        def create_table_info(janela1, ):
            janela1.destroy()
            janela = Tk()
            janela.geometry('1024x768')
            janela.title("Lista")
            janela.iconbitmap("imagens/icone.ico")
            janela.config(background='white')
            header = Label(janela, text='Preencha o formulário.',font=('Arial', 35), background='white')
            header.pack(padx=10, pady=10) 
            txt_box_name_table = Label(janela, text='Nome da tabela.',font=('Arial', 18), background='white')
            txt_box_name_table.pack(padx=5, pady=8)
            inbox_name_table = Entry(janela, width=22, font=('Arial', 16), background='white')
            inbox_name_table.pack(padx=15, pady=5)
            txt_box_column_one = Label(janela, text='Nome da 1º coluna.',font=('Arial', 18), background='white')
            txt_box_column_one.pack(padx=5, pady=8)
            inbox_column_one = Entry(janela, width=22, font=('Arial', 16), background='white')
            inbox_column_one.pack(padx=15, pady=5)
            txt_box_column_two = Label(janela, text='Nome da 2º coluna.',font=('Arial', 18), background='white')
            txt_box_column_two.pack(padx=5, pady=8)
            inbox_box_column_two = Entry(janela, width=22, font=('Arial', 16), background='white')
            inbox_box_column_two.pack(padx=15, pady=5)
            txt_box_column_three = Label(janela, text='Nome da 3º coluna.',font=('Arial', 18), background='white')
            txt_box_column_three.pack(padx=5, pady=8)
            inbox_column_three = Entry(janela, width=22, font=('Arial', 16), background='white')
            inbox_column_three.pack(padx=15, pady=5)
            txt_column_four = Label(janela, text='Nome da 4º coluna.',font=('Arial', 18), background='white')
            txt_column_four.pack(padx=5, pady=8)
            inbox_column_four = Entry(janela, width=22, font=('Arial', 16), background='white')
            inbox_column_four.pack(padx=15, pady=5)
            button_next = Button(janela, text='Executar',width=15, background='blue', font=('Arial', 16), fg ='white' )
            button_next["command"] = lambda text_box_name = inbox_name_table, column1 = inbox_column_one, column2 = inbox_box_column_two, column3 = inbox_column_three , column4 = inbox_column_four: create_table(text_box_name, column1, column2, column3, column4 )
            button_next.pack(padx=15, pady=8)
            messagebox.showinfo("Aviso!", "Favor usar o _ (Underline) para o espaçamento")
            
            
    Windows.mainloop()
   
screen()