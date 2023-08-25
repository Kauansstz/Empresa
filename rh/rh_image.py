from tkinter import Tk, Label, Button, Entry, ttk, messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

def pay_payslip(Windows1):
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry('1024x768')
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

    # Cria um rótulo para exibir a imagem carregada
    image_label =Label(Windows)
    image_label.pack(padx=10, pady=50)