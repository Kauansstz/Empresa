from tkinter import Tk, Label, Button

def tela():
    janela = Tk()
    janela.geometry('500x500')
    janela.title("Lista")
    janela.iconbitmap("imagens/icone.ico")
    janela.mainloop()
    
    btn = Button(janela, text='Executar !', bd = '5', command = janela.destroy)
    btn.pack(side = 'top')

tela()