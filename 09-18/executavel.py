import tkinter
import tkinter.messagebox
from typing import TYPE_CHECKING
import sqlalchemy

class App:
    def __init__(self):
        self.window = tkinter.Tk()
        self.lbl_servidor = tkinter.Label(self.window, text='Servidor')
        self.lbl_servidor.pack()
        self.ent_servidor = tkinter.Entry(self.window)
        self.ent_servidor.insert(0, '127.0.0.1')
        self.ent_servidor.pack()
        self.lbl_porta = tkinter.Label(self.window, text='Porta')
        self.lbl_porta.pack()
        self.ent_porta = tkinter.Entry(self.window)
        self.ent_porta.insert(0, '3050')
        self.ent_porta.pack()
        self.lbl_banco = tkinter.Label(self.window, text='Banco')
        self.lbl_banco.pack()
        self.ent_banco = tkinter.Entry(self.window)
        self.ent_banco.pack()
        self.lbl_usuario = tkinter.Label(self.window, text='Usuário')
        self.lbl_usuario.pack()
        self.ent_usuario = tkinter.Entry(self.window)
        self.ent_usuario.insert(0, 'SYSDBA')
        self.ent_usuario.pack()
        self.lbl_senha = tkinter.Label(self.window, text='Senha')
        self.lbl_senha.pack()
        self.ent_senha = tkinter.Entry(self.window)
        self.ent_senha.insert(0, 'masterkey')
        self.ent_senha.pack()
        self.btn_conectar = tkinter.Button(self.window, text='Conectar', command=self.btn_conectar_onclick)
        self.btn_conectar.pack()

    def btn_conectar_onclick(self):
        self.conectar_banco()

    def execute(self):
        self.window.mainloop()

    def conectar_banco(self):
        engine = sqlalchemy.create_engine(f'firebird+fdb://{self.ent_usuario.get()}:{self.ent_senha.get()}@{self.ent_servidor.get()}:{self.ent_porta.get()}/{self.ent_banco.get()}')
        connection = engine.connect()
        result = connection.execute('SELECT COUNT(1) FROM EMPRESA')
        tkinter.messagebox.showinfo(message=f'Este banco tem {result} empresa(s)')

if __name__ == '__main__':
    App().execute()