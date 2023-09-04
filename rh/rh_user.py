import rh_panel
from rh_consult import select
from rh_create_user import create_user
from tkinter import Tk, Label, Button

def user(Windows1):
    # Panel dedicated only for creating and consulting Users
    Windows1.destroy()    
    Windows = Tk()
    Windows.geometry('1024x768')
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background='white')
    
    txt_tittle = Label(Windows, text="Painel do Funcionário", background="white", font=('Arial', 30))
    txt_tittle.pack(padx=10, pady=30)
    
    button_alter_user = Button(Windows, text='Consulta de Usuários', font=('Arial', 20), background='blue', fg='white', width=20,)
    button_alter_user["command"] = lambda button_alter_user=button_alter_user: select(Windows)
    button_alter_user.pack(padx=10, pady=30)
    
    button_create_user = Button(Windows, text='Criar Login', font=('Arial', 20), background='blue', fg='white', width=20,)
    button_create_user["command"] = lambda button_create_user=button_create_user: create_user(Windows)
    button_create_user.pack(padx=10, pady=30)
    
    button_back = Button(Windows, text='Voltar', font=('Arial', 20), background='blue', fg='white', width=20)
    button_back["command"] = lambda button_back=button_back: open_rh_panel_one(Windows)
    button_back.pack(padx=10, pady=30)
    
    def open_rh_panel_one(self):
        rh_panel.main_panel(self)