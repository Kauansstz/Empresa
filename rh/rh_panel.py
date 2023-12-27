from database import banco
from rh_image import pay_payslip
from rh_user import user
from tkinter import Tk, Label, Button, messagebox


def main_panel(Windows1, login="", senha=""):
    # After logging in, you will go to the menu screen where there are 2 buttons,
    # We have the "Employees" button where we can create or modify the user and the "Launch Payslip" button, having to put the requested information and launch the images
    flag = False

    try:
        result = banco.sql_query(
            f"""SELECT count(*) FROM tb_login WHERE login = {login} and senha = {senha}""",
        )

        if result[0][0] == 1:
            flag = True
    except:
        flag = True
    if flag:
        Windows1.destroy()
        Windows = Tk()
        Windows.geometry("1440x1080")
        Windows.title("Rh_Acesso")
        Windows.iconbitmap("imagens/rh.ico")
        Windows.config(background="white")

        txt_tittle = Label(
            Windows, text="Painel Principal", background="white", font=("Arial", 30)
        )
        txt_tittle.pack(padx=10, pady=10)

        button_image = Button(
            Windows,
            text="Lançar Holerite",
            font=("Arial", 20),
            background="blue",
            fg="white",
            width=20,
        )
        button_image["command"] = lambda button_image=button_image: pay_payslip(Windows)
        button_image.pack(padx=10, pady=50)

        button_create_user = Button(
            Windows,
            text="Funcionário",
            font=("Arial", 20),
            background="blue",
            fg="white",
            width=20,
        )
        button_create_user["command"] = lambda button_image=button_image: user(Windows)
        button_create_user.pack(padx=10, pady=50)

    else:
        messagebox.showerror("Erro!", "Login ou Senha incorretos")
