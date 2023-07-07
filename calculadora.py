from tkinter import Tk, Entry, Label, Button

def tela():
    janela = Tk()
    janela.geometry('400x600')
    janela.title('Calculadora')
    janela.iconbitmap("imagens/calc.ico")
    janela.config(background='black')
    # Caixa de Entrada
    entrada = Entry(janela, background='White', fg='green', font=('Arial', 50))
    entrada.place(x=0, y=50, width=900, height=60)
    # Caixa de Entrada
    # Configuração dos números
    bnt1 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='1', height=2)
    bnt1.place(x=5, y=465)
    bnt2 = Button(janela, background='grey', font=('Arial', 16),width=8, fg='White', text='2', height=2)
    bnt2.place(x=115, y=465)
    bnt3 = Button(janela, background='grey', font=('Arial', 16),width=8, fg='White', text='3', height=2)
    bnt3.place(x=225, y=465)
    bnt5 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='4',height=2)
    bnt5.place(x=5, y=395)
    bnt6 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='5',height=2)
    bnt6.place(x=115, y=395)
    bnt7 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='6',height=2)
    bnt7.place(x=225, y=395)
    bnt8 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='7',height=2)
    bnt8.place(x=5, y=325)
    bnt9 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='7',height=2)
    bnt9.place(x=5, y=325)
    bnt11 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='7',height=2)
    bnt11.place(x=5, y=325)
    # Configuração dos números
    # Configuração dos sinais
    bnt4 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='+',height=2)
    bnt4.place(x=335, y=465)
    bnt10 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='-',height=2)
    bnt10.place(x=335, y=395)
     # Configuração dos sinais
    janela.mainloop()
tela()