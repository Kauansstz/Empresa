from tkinter import *

def mostrar_texto():
    texto = entry.get()
    print(texto)

janela = Tk()

entry = Entry(janela)
entry.pack()

botao = Button(janela, text="Mostrar", command=mostrar_texto)
botao.pack()

janela.mainloop()
