import rh_panel

from tkinter import Tk, Label, Button, Entry, ttk, messagebox

def screen():
    Windows = Tk()
    Windows.geometry('1024x768')
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background='white')
    
    txt_tittle = Label(Windows, text="Recursos Humanos", background="white", font=('Arial', 32))
    txt_tittle.pack(padx=100, pady=100)
    
    txt_logout = Label(Windows, text="Login", background="white", font=('Arial', 20))
    txt_logout.pack(padx=10, pady=10)
    inbox_logout = Entry(Windows, text="Login", font=('Arial',15), background='white')
    inbox_logout.pack(padx=10, pady=10)
    
    txt_password = Label(Windows, text="Senha", background="white", font=('Arial', 20))
    txt_password.pack(padx=10, pady=10)
    inbox_password = Entry(Windows, font=('Arial',15), background='white', show='*')
    inbox_password.pack(padx=10, pady=10)
    
    button_logout = Button(Windows, text='Entrar', font=(16), background='blue', fg='white', width=20)
    button_logout["command"] = lambda login=inbox_logout, senha = inbox_password: open_rh_panel_one(Windows, login.get().upper(),senha.get().upper())
    button_logout.pack(padx=10, pady=50)
    
    def open_rh_panel_one(Windows, login, senha):
        rh_panel.main_panel(Windows, login, senha)
    Windows.mainloop()
screen()