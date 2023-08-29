from database import banco
import main_panel
import tkinter as tk
from tkinter import Tk, Button, ttk, messagebox

def consult_info(Windows1 ):
            # search the database if the table exists and will return with the data
            result = banco.sql_query(f"""SELECT * FROM list_jogos """)
            
            if len(result[0][0]) > 1:
                    Windows1.destroy()
                    Windows = Tk()
                    Windows.geometry('1024x768')
                    Windows.title("Lista")
                    Windows.iconbitmap("imagens/icone.ico")
                    Windows.config(background='white')
                    table = ttk.Treeview(Windows, selectmode="extended", columns=("col1", "col2", "col3", "col4"))
                    table.grid(row=0, column=0, sticky="nsew")
                    table.heading("col1", text="coluna1" )
                    table.heading("col2", text="coluna2")
                    table.heading("col3", text="coluna3")
                    table.heading("col4", text="coluna4")
                    table.column("#0", width=0, stretch=tk.NO)
                    table.column("col1", width=450)
                    table.column("col2", width=140)
                    table.column("col3", width=100)
                    table.column("col4", width=100)
                    for i in result:
                        table.insert("", "end", values=(i[0], i[1], i[2], i[3]))
                        print(i)
                    scrollbar = ttk.Scrollbar(Windows, orient="vertical", command="table.yview")
                    scrollbar.grid(row=0, column=1, sticky="ns")
                    table.configure(yscrollcommand=scrollbar.set)
                    Windows.grid_rowconfigure(0, weight=1)
                    Windows.grid_columnconfigure(0, weight=1)
                    button_back= Button(Windows, text="Voltar", background='blue', fg='white', font=('Arial', 18), width=10)
                    button_back["command"]= lambda botao8=button_back: open_menu_four(Windows)
                    button_back.place(x=500, y= 500)   
            else:
                messagebox.showerror("Erro!", "Tabela inexistente")
            return result
def open_menu_four(self):
    main_panel.menu(self)
