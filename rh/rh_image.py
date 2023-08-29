import rh_panel
import tkinter as tk
from tkinter import Tk, Label, Button, Entry, messagebox, ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def pay_payslip(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry('1440x1080')
    Windows.title("Rh_Acesso")
    Windows.iconbitmap("imagens/rh.ico")
    Windows.config(background='white')
    
    def open_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")])
            if file_path:
                image = Image.open(file_path)
                photo = ImageTk.PhotoImage(image)
                image_label.config(image=photo)
                image_label.photo = photo
            
    load_image = Button(Windows, text="Carregar Imagem", command=open_image)
    load_image.pack(padx=10, pady=50)
    image_label =Label(Windows)
    image_label.pack(padx=10, pady=50)
    def on_scroll(*args):
                canvas.yview(*args)
                text.yview(*args)
                canvas = tk.Canvas(Windows)
                canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)   
                scrollbar = tk.Scrollbar(Windows, command=on_scroll)
                scrollbar.pack(side=tk.LEFT, fill=tk.Y) 
                text = tk.Text(canvas, yscrollcommand=scrollbar.set)
                text.pack(fill=tk.BOTH, expand=True)
                canvas.create_window(0, 0, anchor=tk.NW, window=text)
                canvas.update_idletasks()
                canvas.config(scrollregion=canvas.bbox(tk.ALL))
                
    # Cria um rótulo para exibir a imagem carregada
    
    button_exe = Button(Windows, text='Executar', font=('Arial', 20), background='blue', fg='white', width=10)
    button_exe.pack(padx=10, pady=50)
    button_back = Button(Windows, text='Voltar', font=('Arial', 20), background='blue', fg='white', width=10)
    button_back["command"] = lambda button_back=button_back: open_panel_one(Windows)
    button_back.pack(padx=10, pady=50)

def open_panel_one(self):
    rh_panel.main_panel(self)