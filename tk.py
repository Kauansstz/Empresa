import banco
import login
from tkinter import Tk, Label, Button, Pack, Entry, PhotoImage, ttk
from PIL import ImageTk, Image

def usuario(a,b):
    result = login.usuario(a,b)
    if result[0][0] == 1:
        print('Bem vindo')
    else:
        print('Nao')
    usuario()
def tela():
    # Configuração Janela
    janela = Tk()
    janela.geometry('1024x768')
    janela.title("Lista")
    janela.iconbitmap("imagens/icone.ico")
    janela.config(background='white')
    entrada = btn.get()
    # Configuração da Janela

    img = Image.open("C:/Users/V/Desktop/projeto/imagens/paisagem.jpg")
    img = img.resize((1600,980))
    img_tk = ImageTk.PhotoImage(img)
    img_label = Label(janela, image=img_tk)
    img_label.place(x=0, y=0)

    txt1 = Label(janela, text='Lista', font=('Arial',42, ), background='white')
    txt1.pack(padx=80, pady=80)

    txt2 = Label(janela, text='Login', font=('Arial',15), background='white')
    txt2.pack(padx=15, pady=10)

    caixa1 = Entry(janela, text="Login", font=('Arial',15))
    caixa1.pack(padx=12, pady=8)

    txt3 = Label(janela, text='Senha', font=('Arial',15), background='white')
    txt3.pack(padx=15, pady=10)

    caixa2 = Entry(janela, text="senha", font=('Arial',15), background='white')
    caixa2.pack(padx=12, pady=8)

    btn = Button(janela, text='Entrar', font=(16), background='#4798e8', fg='white', command=usuario )
    btn.pack(padx=25, pady=30)
   
    lb = Label(janela, text="Esqueci a minha senha", font=('Arial black', 10), fg='blue')
    lb.config(bg=janela['bg'])
    lb.pack(padx=40, pady=45)
    # Configuração das Imagens
    imagem = Image.open("C:/Users/V/Desktop/projeto/imagens/cadeado.ico")
    imagem = imagem.resize((25, 25))  
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = Label(janela, image=imagem_tk)
    label_imagem.place(x=651, y=559)

    

    # Configuração das Imagens

    
   
    janela.mainloop()
   

tela()