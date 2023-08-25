from banco import sql_query
from insert import insert
from delete import delete_info
from consult import consult_info
from tkinter import Tk, Label, Button, messagebox

def menu(Windows1, login = '', password =''):
        #After logging in, you will go to the menu screen where there are 4 buttons, 
        # where you have the button to insert, delete and consult the data and the fourth button, which serves to create tables
        flag= False
        
        try:
            result = sql_query(f"""SELECT count(*) FROM tb_login WHERE login = '{login.get().upper()}' and senha = '{password.get().upper()}'""")
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
            button_insert = Button(Windows, text='Inserir', font=('Arial', 20), background='white', width= 20)
            button_insert["command"] = lambda botao1=button_insert: insert(Windows)
            button_insert.pack(padx=10, pady=50)
            button_query = Button(Windows, text='Consultar', font=('Arial', 20), background='white', width= 20)
            button_query["command"] = lambda botao2=button_query: consult_info( Windows)
            button_query.pack(padx=10, pady=50)
            button_delete  = Button(Windows, text='Deletar', font=('Arial', 20), background='white', width= 20)
            button_delete ["command"] = lambda botao3=button_delete : delete_info(Windows)
            button_delete.pack(padx=10, pady=50)
            
        else:
            text_box_error = Label( text='Não possui cadastro? Favor entrar em contato com o administrador.', font=('Arial',15), background='white')
            text_box_error.pack(padx=15, pady=10)
            messagebox.showerror("Error!", "Login ou Senha incorreto!")

        
