# from database import banco
from database import banco_server
from rh_image import pay_payslip
from rh_user import create_user
from tkinter import Tk, Label, Button, Entry, ttk, messagebox

def main_panel(Windows1,login='', senha=''):
        resultado = banco_server.sql_server_query(f"""SELECT COUNT(*) FROM tb_login_rh WHERE usuario = '{login}' AND senha = '{senha}' """)
        if resultado[0][0] == 1:
            Windows1.destroy()
            Windows = Tk()
            Windows.geometry('1440x1080')
            Windows.title("Rh_Acesso")
            Windows.iconbitmap("imagens/rh.ico")
            Windows.config(background='white')
            
            txt_tittle = Label(Windows, text="Painel Principal", background="white", font=('Arial', 30))
            txt_tittle.pack(padx=10, pady=10)
            
            button_image = Button(Windows, text='Lançar Holerite', font=('Arial', 20), background='blue', fg='white', width=20,)
            button_image["command"] = lambda : pay_payslip(Windows)
            button_image.pack(padx=10, pady=50)
            
            button_create_user = Button(Windows, text='Funcionário', font=('Arial', 20), background='blue', fg='white', width=20,)
            button_create_user["command"] = lambda : create_user(Windows)
            button_create_user.pack(padx=10, pady=50)
    
        else:
            messagebox.showerror("Erro!", "Login ou Senha incorretos")