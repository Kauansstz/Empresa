import banco
from main import menu
from tkinter import Tk, Label, Button, Entry, ttk, messagebox

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
            inbox_name_game = Entry(Windows, width=22, font=('Arial', 16), background='white', fg='white')
            inbox_name_game.place(x=250, y=190)
            box_text_level = Label(Windows, text='Nivel do Jogo.',font=('Arial', 18), background='white')
            box_text_level.place(x=250, y=240)
            inbox_level = Entry(Windows, width=22, font=('Arial', 16), background='white', fg='white')
            inbox_level.place(x=250, y=270)
            game_hours_text_box = Label(Windows, text=' Horas de jogo.',font=('Arial', 18), background='white')
            game_hours_text_box.place(x=600, y= 150)
            game_hours_inbox = Entry(Windows, width=22, font=('Arial', 16), background='white', fg='white')
            game_hours_inbox.place(x=600, y=190)
            total_hours_played_txt_box = Label(Windows, text='Total de Horas jogadas.',font=('Arial', 18), background='white')
            total_hours_played_txt_box.place(x=600, y=240)
            total_hours_played_inbox = Entry(Windows, width=22, font=('Arial', 16), background='white')
            total_hours_played_inbox.place(x=600, y=270)
            execute_button = Button(Windows, text='Executar',width=15, background='blue', font=('Arial', 16), fg ='white' )
            execute_button["command"] = lambda name_game=inbox_name_game, level=inbox_level, game_hours=game_hours_inbox, total_hours= total_hours_played_inbox: enter(name_game.get(),
                                                                                                                                                                       level.get(), 
                                                                                                                                                                       game_hours.get(),
                                                                                                                                                                       total_hours.get())
            execute_button.place(x=550, y=400)
            butoon_back = Button(Windows, text='Voltar', width=15, background='blue', font=('Arial', 16), fg='white')
            butoon_back["command"] = lambda botao7=butoon_back: open_menu_one(Windows)
            butoon_back.place(x=300, y=400)
            
            
            # Inserting information in the insert function and sending it to the enter function and including data in the table
            
            def enter(name_game, level, game_hours, total_hours):
                    banco.sql_inserir(f"""INSERT INTO list_jogos
                                ( NOME_JOGO,
                                DIFICULDADE,
                                QTN_HORAS,
                                TOTAL_HORAS) 
                                VALUES('{name_game}'
                                        ,'{level}', 
                                        {game_hours},
                                        {total_hours} )""")
                    messagebox.showinfo("Aviso!", "Dados Inseridos!")

def open_menu_one(self):
        menu(self)