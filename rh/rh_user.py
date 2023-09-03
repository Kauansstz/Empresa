import rh_panel
from database import banco_server
import cx_Oracle
from tkinter import Tk, Label, Button, Entry, messagebox


def create_user(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry('1440x1080')
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background='white')
    
    txt_tittle = Label(Windows, text="Preencha o Formulário", background="white", font=('Arial', 30))
    txt_tittle.place(x=550, y=50 )
    
    txt_name = Label(Windows, text="Nome Completo", background="white", font=('Arial', 20))
    txt_name.place(x=100, y=200)
    inbox_name = Entry(Windows, text="Login", font=('Arial',15), background='white')
    inbox_name.place(x=100, y=250 )
    
    txt_mail = Label(Windows, text="Email", background="white", font=('Arial', 20))
    txt_mail.place(x=400, y=200)
    inbox_mail = Entry(Windows, font=('Arial',15), background='white')
    inbox_mail.place(x=400, y=250)
    
    txt_registration = Label(Windows, text="Mátricula", background="white", font=('Arial', 20))
    txt_registration.place(x=700, y=200)
    inbox_registration = Entry(Windows,  font=('Arial',15), background='white')
    inbox_registration.place(x=700, y=250)
    
    
    txt_sector = Label(Windows, text="Setor", background="white", font=('Arial', 20))
    txt_sector.place(x=1000, y=200)
    inbox_sector = Entry(Windows, font=('Arial',15), background='white')
    inbox_sector.place(x=1000, y=250)
    
    txt_office = Label(Windows, text="Cargo", background="white", font=('Arial', 20))
    txt_office.place(x=100, y=350)
    inbox_office = Entry(Windows, font=('Arial',15), background='white')
    inbox_office.place(x=100, y=400)

    txt_login = Label(Windows, text="Login", background="white", font=('Arial', 20))
    txt_login.place(x=400, y=350)
    inbox_login = Entry(Windows,  font=('Arial',15), background='white')
    inbox_login.place(x=400, y=400)
    
    txt_password = Label(Windows, text="Senha", background="white", font=('Arial', 20))
    txt_password.place(x=700, y=350)
    inbox_password = Entry(Windows,  font=('Arial',15), background='white')
    inbox_password.place(x=700, y=400)

    txt_store = Label(Windows, text="Loja", background="white", font=('Arial', 20))
    txt_store.place(x=1000, y=350)
    inbox_store = Entry(Windows, font=('Arial',15), background='white')
    inbox_store.place(x=1000, y=400)
    
    button_exe = Button(Windows, text='Executar', font=('Arial', 16), background='blue', fg='white', width=20)
    button_exe["command"] = lambda name=inbox_name, mail = inbox_mail,  login = inbox_login, password = inbox_password, office = inbox_office, sector = inbox_sector,  registration = inbox_registration, store = inbox_store : inserted(name.get(),
                                                                                                                                                                mail.get(),
                                                                                                                                                                login.get(),
                                                                                                                                                                password.get(),
                                                                                                                                                                office.get(),
                                                                                                                                                                sector.get(),
                                                                                                                                                                registration.get(),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                store.get())
    button_exe.place(x=650, y=600 )
    button_back = Button(Windows, text='Voltar', font=('Arial', 16), background='blue', fg='white', width=20)
    button_back["command"] = lambda button_back=button_back: open_panel(Windows)
    button_back.place(x=650, y=650 )
    
def open_panel(self):
    rh_panel.main_panel(self)
    
def inserted(name, mail, login, password, office, sector, registration,store):
    try:
        banco_server.sql_server_insert(f"""INSERT INTO tb_funcionarios(
                                NOME_COMPLETO,
                                EMAIL,
                                LOGIN,
                                SENHA,
                                CARGO,
                                SETOR,
                                MATRICULA,
                                LOJA
                        )
                                VALUES (
                                    '{name.upper()}',
                                    '{mail.upper()}',
                                    '{login.upper()}',
                                    '{password.upper()}',
                                    '{office.upper()}',
                                    '{sector.upper()}',
                                    '{registration.upper()}',
                                    '{store.upper()}')
                            """)
        messagebox.showinfo("Aviso!", "Usuário Criado com Sucesso!")
    except cx_Oracle.DatabaseError as e :
                error, = e.args
                messagebox.showerror("Erro no Banco de Dados", f"Ocorreu um erro no banco de dados:\n{error.message}")

