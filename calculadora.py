from tkinter import Tk, Entry, Label, Button, PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
import json




def tela():
    with open('dados.json', 'r') as file:
        cor = json.load(file)

    janela = Tk()
    janela.geometry('400x600')
    janela.title('Calculadora')
    janela.iconbitmap("imagens/calc.ico")
    janela.config(background=cor["cor"])

    # Caixa de Entrada
    entrada = Entry(janela, background='White', fg='green', font=('Arial', 50))
    entrada.place(x=0, y=50, width=900, height=60)

    # Caixa de Entrada
    # Configuração dos números
    bnt1 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='1', height=2)
    bnt1["command"] = lambda num1=bnt1 : somar()
    bnt1.place(x=5, y=465)
    bnt2 = Button(janela, background='grey', font=('Arial', 16),width=8, fg='White', text='2', height=2)
    bnt2.place(x=115, y=465)
    bnt2["command"] = lambda num2=bnt1 : somar()
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
    bnt9 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='8',height=2)
    bnt9.place(x=115, y=325)
    bnt11 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='9',height=2)
    bnt11.place(x=225, y=325)
    bnt14 = Button(janela, background='gray', font=('Arial', 16),width=8, fg='White', text='0',height=2)
    bnt14.place(x=115, y=535)
    # Configuração dos números
    # Configuração dos sinais
    bnt4 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='+',height=2)
    bnt4.place(x=335, y=465)
    bnt10 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='-',height=2)
    bnt10.place(x=335, y=395)
    bnt12 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='x',height=2)
    bnt12.place(x=335, y=325)
    bnt13 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='+/-',height=2)
    bnt13.place(x=5, y=535)
    bnt15 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text=',',height=2)
    bnt15.place(x=225, y=535)
    bnt15 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='white', text='=',height=2)
    bnt15.place(x=335, y=535)
    bnt19 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='÷',height=2)
    bnt19.place(x=335, y=255)
     # Configuração dos sinais
     # Configurações dos simbolos 
    bnt16 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='½',height=2)
    bnt16.place(x=5, y=255)
    bnt17 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='x²',height=2)
    bnt17.place(x=115, y=255)
    bnt18 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='√1',height=2)
    bnt18.place(x=225, y=255)
    bnt20 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='%',height=2)
    bnt20.place(x=5, y=185)
    bnt21 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='CE',height=2)
    bnt21.place(x=115, y=185)
    bnt22 = Button(janela, background='light gray', font=('Arial', 16),width=8, fg='black', text='C',height=2)
    bnt22.place(x=225, y=185)
    bnt23 = Button(janela, background='light gray', font=('Arial', 16),width=5, fg='black', text='⌫',height=2)
    bnt23.place(x=335, y=185)
    bnt24 = Button(janela, background='black', font=('Arial', 12),width=7, fg='white', text='MC',height=2, bg = 'black')
    bnt24.place(x=5, y=135)
    bnt25 = Button(janela, background='black', font=('Arial', 12),width=7, fg='white', text='MR',height=2, bg = 'black')
    bnt25.place(x=85, y=135)
    bnt26 = Button(janela, background='black', font=('Arial', 12),width=7, fg='white', text='M+',height=2, bg = 'black')
    bnt26.place(x=165, y=135)
    bnt27 = Button(janela, background='black', font=('Arial', 12),width=7, fg='white', text='MS',height=2, bg = 'black')
    bnt27.place(x=245, y=135)
    bnt28 = Button(janela, background='black', font=('Arial', 12),width=7, fg='white', text='M▼',height=2, bg = 'black')
    bnt28.place(x=325, y=135)
     # Configurações dos simbolos
     # Configuração de Botao
    bnt29 = Button(janela, background='black', font=('Arial',12), text='☰', fg = 'white')
    bnt29["command"] = lambda bnt29=bnt29: menu(janela)
    bnt29.place(x=0, y=0)
     # Configuração de Botao

        
    def Onclick():
        atual = entrada.get()
        if atual:
            return somar()

    def somar(btn=None):
        resultado = bnt1["text"] + bnt2["text"]
        return resultado

    def menu(janela1):
        with open('dados.json', 'r') as file:
            cor = json.load(file)
        janela1.destroy()
        janela = Tk()
        janela.geometry('400x600')
        janela.title('Calculadora')
        janela.iconbitmap("imagens/calc.ico")
        janela.config(background=cor["cor"])

        botao01 = Button(janela, text='Configurações', font=('calibri', 16), width=36, fg = 'white', background='gray')
        botao01["command"] = lambda botao01=botao01: config(janela)
        botao01.place(x=0, y=20)
        botao02 = Button(janela, text='🛈 Sobre', font=('calibri', 16), width=36, fg = 'white', background='gray')
        botao02["command"] = lambda botao02=botao02 : info(janela)
        botao02.place(x=0, y=80)

        def cores(cor):
            if cor["text"] == 'Escuro':
                configura = {'cor': 'black'}
            else:
                configura = {'cor': 'white'}

            with open('dados.json', 'w') as file:
                json.dump(configura, file)


        def config(janela1):
            with open('dados.json', 'r') as file:
                cor = json.load(file)
            janela1.destroy()
            janela = Tk()
            janela.geometry('400x600')
            janela.title('Calculadora')
            janela.iconbitmap("imagens/calc.ico")
            janela.config(background=cor["cor"])
            bt01= Button(janela, text='Escuro', font=('calibri', 16), background='black', fg='white')
            bt01["command"]= lambda cor= bt01 : cores(cor)
            bt01.place(x=10, y=100)
            bt02= Button(janela, text='Claro', font=('calibri', 16), background='black', fg='white')
            bt02["command"]= lambda cor= bt02 : cores(cor)
            bt02.place(x=150, y=150)

            

    def info(janela1):
        with open('dados.json', 'r') as file:
            cor = json.load(file)
        janela1.destroy()
        janela = Tk()
        janela.geometry('400x600')
        janela.title('Calculadora')
        janela.iconbitmap("imagens/calc.ico")
        janela.config(background=cor["cor"])
        txt = Label(janela, text='Calculadora 11.2210.0.0\n© 2022 Microsoft. Todos os direitos reservados.', font=('calibri', 12), background='black', fg='white')
        txt.place(x=10, y=100)
        txt1 = Label(janela, text='Sobre', font=('calibri', 12), background='black', fg='white')
        txt1.place(x=10, y=50)
        txt2 = Label(janela, text='Termos de Licença para Software Microsoft', font=('calibri', 12), background='black', fg='#FFDAB9')
        txt2.place(x=10, y=150)
        txt3 = Label(janela, text='Contrato de Serviço Microsoft', font=('calibri', 12), background='black', fg='#FFDAB9')
        txt3.place(x=10, y=180)
        txt4 = Label(janela, text='Política de Privacidade da Microsoft', font=('calibri', 12), background='black', fg='#FFDAB9')
        txt4.place(x=10, y=220)
    janela.mainloop()
tela()