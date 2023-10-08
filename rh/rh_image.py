import rh_panel
from database import banco
import tkinter as tk
from tkinter import Tk, Label, Button, Entry, messagebox
from tkinter import filedialog
import os


def pay_payslip(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry("1440x1080")
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background="white")

    txt_tittle = Label(
        Windows, text="Lançar Holerite", font=("Arial", 35), background="white"
    )
    txt_tittle.pack(padx=0, pady=50)

    txt_name = Label(
        Windows, text="Nome do Funcionário", font=("Arial", 20), background="white"
    )
    txt_name.pack(padx=0, pady=10)
    inbox_name = Entry(Windows, font=("Arial", 15), background="white", width=30)
    inbox_name.pack(padx=0, pady=10)

    txt_month = Label(
        Windows, text="Mês do lançamento", font=("Arial", 20), background="white"
    )
    txt_month.pack(padx=0, pady=10)
    inbox_month = Entry(Windows, font=("Arial", 15), background="white", width=30)
    inbox_month.pack(padx=0, pady=10)

    def browse_image():
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )
        if file_path:
            file_name = os.path.basename(file_path)  # Collecting the file name
            directory = os.path.dirname(file_path)  # collecting file directory/path
            entry_image_path.delete(0, tk.END)  # Clear previous content
            entry_image_path.insert(0, file_name)  # Inserting the image in the Entry.
            entry_image_path.insert(
                0, "/"
            )  # Separating the directory/path with the file name.
            entry_image_path.insert(0, directory)  # Entering directory/path.

    # Variable that receives the 'Entry' property that will show the results of the 'browser_image' function, having the directory/path, the separation with a slash and the file name,
    # Example 'C:\Users\user\Image\Image.png'
    # Button named 'browse_button' that will browse the local computer and get the image that the user will select.
    txt_image = Label(Windows, text="Holerite", font=("Arial", 20), background="white")
    txt_image.pack(padx=0, pady=10)
    entry_image_path = tk.Entry(
        Windows, font=("Arial", 15), background="white", width=30
    )
    entry_image_path.pack(pady=10)
    browse_button = tk.Button(Windows, text="Procurar Imagem", command=browse_image)
    browse_button.pack(pady=50)

    # Button named 'button_exe' will run as soon as it gets the information just above and will send to the 'insert' function.
    # Button named 'button_back' will go back to the 'rh_panel' tab.
    button_exe = Button(
        Windows,
        text="Executar",
        font=("Arial", 20),
        background="blue",
        fg="white",
        width=10,
    )
    button_exe[
        "command"
    ] = lambda month=inbox_month, name_user=inbox_name, image=entry_image_path: insert(
        month.get(), name_user.get(), image.get()
    )
    button_exe.pack(padx=10, pady=10)
    button_back = Button(
        Windows,
        text="Voltar",
        font=("Arial", 20),
        background="blue",
        fg="white",
        width=10,
    )
    button_back["command"] = lambda button_back=button_back: open_panel_one(Windows)
    button_back.pack(padx=10, pady=10)


# The insert function will receive the information just above, it will check if the users table if the typed user exists, if it does not exist, it will give an error with the message from;
# 'User not registered!'.
# If it exists, it will send the information to the SQL Server and insert it in the 'tb_image' table that will store the payslip images.
def insert(month, name_user, image):
    resultado = banco.sql_query(
        f"""SELECT count(*) FROM tb_funcionarios WHERE nome_completo = '{name_user.upper()}'"""
    )
    flag = False
    if resultado[0][0] == 1:
        flag = True
        if flag == True:
            banco.sql_inserir(
                f"""
                                        INSERT INTO dbo.tb_image(mes, nome_usuario, imagem)
                                            SELECT 
                                                '{month.upper()}', '{name_user.upper()}', BULKCOLUMN
                                            FROM OPENROWSET (BULK '{image}', SINGLE_BLOB) AS IMAGEM
    """
            )
            messagebox.showinfo(
                "Aviso!", "Informações do holerite lançado no sistema com sucesso!"
            )
    else:
        messagebox.showerror("Error!", "Usuário não cadastrado!")


def open_panel_one(Windows):
    rh_panel.main_panel(Windows)
