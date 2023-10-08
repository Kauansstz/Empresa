from tkinter import Tk, Label, Button, Entry, messagebox
from database import banco
import rh_consult


def info(Windows1):
    # Tab where you will have the functionality to change the values ​​of a certain column.
    # Example: Changing the registration number of the login 'Kauanss'.
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry("800x800")
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background="white")

    txt_tittle = Label(
        Windows, text="Preencha o Formulário", background="white", font=("Arial", 20)
    )
    txt_tittle.place(x=300, y=50)

    txt_user = Label(Windows, text="Login", background="white", font=("Arial", 20))
    txt_user.place(x=50, y=200)
    inbox_user = Entry(Windows, font=("Arial", 15), background="white")
    inbox_user.place(x=50, y=250)

    txt_name_column = Label(
        Windows, text="Nome da Coluna", background="white", font=("Arial", 20)
    )
    txt_name_column.place(x=300, y=200)
    inbox_name_column = Entry(Windows, font=("Arial", 15), background="white")
    inbox_name_column.place(x=300, y=250)

    txt_info = Label(
        Windows, text="Nova Informação", background="white", font=("Arial", 20)
    )
    txt_info.place(x=550, y=200)
    inbox_info = Entry(Windows, font=("Arial", 15), background="white")
    inbox_info.place(x=550, y=250)

    button_exe = Button(
        Windows,
        text="Executar",
        font=("Arial", 16),
        background="blue",
        fg="white",
        width=20,
    )
    button_exe[
        "command"
    ] = lambda name_column=inbox_name_column, new_info=inbox_info, name_user=inbox_user,: user_alter(
        name_column.get(), new_info.get(), name_user.get()
    )
    button_exe.place(x=300, y=600)
    button_back = Button(
        Windows,
        text="Voltar",
        font=("Arial", 16),
        background="blue",
        fg="white",
        width=20,
    )
    button_back["command"] = lambda button_back=button_back: open_consult(Windows)
    button_back.place(x=300, y=650)


def user_alter(name_column, new_info, name_user):
    banco.sql_inserir(
        f"""UPDATE tb_funcionarios
                                        SET {name_column.upper()} = '{new_info.upper()}'
                                        WHERE usuario = '{name_user.upper()}'
                                        """
    )
    messagebox.showinfo("Aviso!", " Alteração de dados com sucesso!")


def open_consult(self):
    rh_consult.select(self)
