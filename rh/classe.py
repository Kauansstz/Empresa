from database import banco
from rh_panel import main_panel
from tkinter import messagebox

class User:
    def __init__(self, username, password, access_level):
        self.username = username
        self.password = password
        self.access_level = access_level
        
    def database(self, login ='', senha = ''):
        try:
            users_db = banco.sql_query(f"""SELECT COUNT(*) 
                                    FROM TB_LOGIN_RH 
                                    WHERE login = '{login.get().upper()}' AND senha = '{senha.get().upper()}' AND SETOR = 'RH' OR SETOR = 'TI'""")
            for user in users_db:
                    if user.username == login and user.password == senha:
                        return user
        except:
             messagebox.showerror("Error!", "Login ou senha inválidos")
        return open_rh
    
        # def released(username, password):
        #     for user in users_db:
        #         if user.username == username and user.password == password:
        #             return user
        #     return None
    
        # def main():
        #     username = input("Nome de usuário: ")
        #     password = input("Senha: ")

        #     user = released(username, password)
        #     if user:
        #         if user.access_level == 'TI':
        #             print("Bem-vindo, administrador!")
        #             # Faça o que precisa para o nível de administrador
        #         elif user.access_level == 'RH':
        #             print("Bem-vindo, usuário!")
        #             # Faça o que precisa para o nível de usuário
        #     else:
        #         print("Usuário ou senha incorretos.")

def open_rh(self):
        main_panel(self)