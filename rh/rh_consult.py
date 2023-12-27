from database import banco
from tkinter import Tk, Button, ttk, messagebox
import rh_user
import rh_user_alter
import tkinter as tk


def select(Windows1):
    result = banco.sql_query(f"""SELECT * FROM tb_rh""")

    if result[0][0] == 1:
        Windows1.destroy()
        Windows = Tk()
        Windows.geometry("1440x600")
        Windows.title("Rh_Acesso")
        Windows.iconbitmap("imagens/rh.ico")
        Windows.config(background="white")

        table = ttk.Treeview(
            Windows,
            selectmode="extended",
            columns=(
                "ID",
                "Nome",
                "Email",
                "Mátricula",
                "Setor",
                "Cargo",
                "Loja",
                "Usuário",
                "Senha",
            ),
        )
        table.grid(row=0, column=0, sticky="nsew")
        table.heading("ID", text="ID")
        table.heading("Nome", text="Nome")
        table.heading("Email", text="Email")
        table.heading("Mátricula", text="Mátricula")
        table.heading("Setor", text="Setor")
        table.heading("Cargo", text="Cargo")
        table.heading("Loja", text="Loja")
        table.heading("Usuário", text="Usuário")
        table.heading("Senha", text="Senha")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("ID", minwidth=0, width=50)
        table.column("Nome", minwidth=0, width=300)
        table.column("Email", minwidth=0, width=300)
        table.column("Mátricula", minwidth=0, width=80)
        table.column("Setor", minwidth=0, width=80)
        table.column("Cargo", minwidth=0, width=100)
        table.column("Loja", minwidth=0, width=100)
        table.column("Usuário", minwidth=0, width=100)
        table.column("Senha", minwidth=0, width=80)
        for i in result:
            table.insert(
                "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            )
        scrollbar = ttk.Scrollbar(Windows, orient="vertical", command="table.yview")
        scrollbar.grid(row=0, column=1, sticky="ns")
        table.configure(yscrollcommand=scrollbar.set)
        Windows.grid_rowconfigure(0, weight=1)
        Windows.grid_columnconfigure(0, weight=1)
        button_advence = Button(
            Windows,
            text="Alteração de Dados",
            background="blue",
            fg="white",
            font=("Arial", 18),
            width=20,
        )
        button_advence["command"] = lambda button_advence=button_advence: open_alter(
            Windows
        )
        button_advence.place(x=500, y=400)
        button_back = Button(
            Windows,
            text="Voltar",
            background="blue",
            fg="white",
            font=("Arial", 18),
            width=20,
        )
        button_back["command"] = lambda botao8=button_back: open_user(Windows)
        button_back.place(x=500, y=500)

    else:
        messagebox.showerror("Erro!", "Tabela inexistente")


def open_alter(self):
    rh_user_alter.info(self)


def open_user(self):
    rh_user.user(self)
