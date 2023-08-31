import rh_panel
import tkinter as tk
from tkinter import Tk, Label, Button
from tkinter import filedialog
import os

def pay_payslip(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry('1440x1080')
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background='white')
    
    txt_tittle = Label(Windows, text='Lançar Holerite', font=('Arial', 35), background='white')
    txt_tittle.pack(padx=0, pady=50)
    
    def browse_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
        if file_path:
            file_name = os.path.basename(file_path)
            entry_image_path.delete(0, tk.END)  # Limpar o conteúdo anterior
            entry_image_path.insert(0, file_name)
            
    entry_image_path = tk.Entry(Windows, width=50)
    entry_image_path.pack(pady=10)

    browse_button = tk.Button(Windows, text="Procurar Imagem", command=browse_image)
    browse_button.pack(pady=50)
    
    button_exe = Button(Windows, text='Executar', font=('Arial', 20), background='blue', fg='white', width=10)
    button_exe.pack(padx=10, pady=10)
    button_back = Button(Windows, text='Voltar', font=('Arial', 20), background='blue', fg='white', width=10)
    button_back["command"] = lambda button_back=button_back: open_panel_one(Windows)
    button_back.pack(padx=10, pady=10)

def open_panel_one(self):
    rh_panel.main_panel(self)