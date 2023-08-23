# import banco
from tkinter import Tk, Label, Button, Entry, ttk, messagebox

def screen():
    Windows = Tk()
    Windows.geometry('1024x768')
    Windows.title("Lista")
    Windows.iconbitmap("imagens/icone.ico")
    Windows.config(background='white')
    
    txt_tittle = Label(Windows, text="Recursos Humanos", background="white", font=('Arial', 32))
    txt_tittle.pack(padx=100, pady=100)
    
    Windows.mainloop()
screen()