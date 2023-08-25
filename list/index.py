import main
from tkinter import Tk, Label, Button, Entry

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
    enter_button["command"] = lambda login=inbox_user, password=inbox_password: open_menu(Windows,login, password)
    enter_button.pack(padx=25, pady=30)
    
    
    def open_menu(self,login, password):
        main.menu(self,login, password)
            
    Windows.mainloop()
   
screen()