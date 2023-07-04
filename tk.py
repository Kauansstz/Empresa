from tkinter import Tk, Label, Button, Pack, Entry, PhotoImage
from PIL import ImageTk, Image

def tela():
    janela = Tk()
    janela.geometry('500x500')
    janela.title("Lista")
    janela.iconbitmap("imagens/icone.ico")
    janela.configure(background="white")
    imagem = Image.open(file='C:/Users/V/Downloads/pato.jpg')
    imagem_redi = imagem.resize((500,500))
    imagem_tk = ImageTk.PhotoImage(imagem_redi)
    imagem_tk = Image
    label_imagem = Label(janela, image=imagem_tk)
    label_imagem.place(x=0, y=0, height=1, width= 1)

    txt1 = Label(janela, text='Lista', font=('Arial',42), background='white')
    txt1.pack(padx=20, pady=50)

    txt2 = Label(janela, text='Login', font=('Calibri',15), background='white')
    txt2.pack(padx=15, pady=10)

    caixa1 = Entry(janela, text="Login", font=('Calibri',15), background='white')
    caixa1.pack(padx=12, pady=8)

    txt3 = Label(janela, text='Senha', font=('Calibri',15), background='white')
    txt3.pack(padx=15, pady=10)

    caixa2 = Entry(janela, text="Login", font=('Calibri',15), background='white')
    caixa2.pack(padx=12, pady=8)

    btn = Button(janela, text='Entrar', font=(16), background='#00009C', fg='white')
    btn.pack(padx=25, pady=30)
   
    janela.mainloop()
   

tela()