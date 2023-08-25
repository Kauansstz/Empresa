import banco
from main import menu
from tkinter import Tk, Label, Button, Entry, messagebox
def delete(name):
            banco.sql_inserir(f"""DELETE FROM list_jogos WHERE nome_jogo = '{name}'""")
            messagebox.showinfo("Atenção!", "Dados deletados!")
            return 'Deletado com sucesso'
        
def delete_info( Windows1):
    # The function will collect column name and directly delete in database
    Windows1.destroy()
    Windows = Tk()
    Windows.geometry('1024x768')
    Windows.title("Lista")
    Windows.iconbitmap("imagens/icone.ico")
    Windows.config(background='white')
    txt = Label(Windows, text=' Digite o nome da primeira coluna para deletar.',font=('Arial', 18), background='white')
    txt.place(x=290,y=200)
    caixa_txt = Entry(Windows,width=28 ,font=('Arial',18))
    caixa_txt.place(x=304, y=300)

    botao4= Button(Windows,text="Executar",font=('Arial',18), background='blue', fg='white', width=10)
    botao4["command"] = lambda name=caixa_txt: delete(name.get())
    botao4.place(x= 500, y= 400)
    botao5= Button(Windows,text="Voltar",font=('Arial',18), background='blue', fg='white', width=10)
    botao5["command"] = lambda botao5=botao5: open_menu_three(Windows)
    botao5.place(x= 320, y= 400)

def open_menu_three(self):
    menu(self)