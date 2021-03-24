import mysql.connector
import os
import sys

# Classe responsável pela conexão ao banco de dados

class Conexao:
    def __init__(self):
        try:
            self.conectar = mysql.connector.connect(host="localhost", user="root", database="db_farmacia", password="")
        except mysql.connector.Error as e:
            print(e)
        return self.conectar

    def ConsultarTabela(self, consulta):
        try:
            self.cursor = self.conexao_db()
            lista = self.cursor.execute("SELECT nome_produto, preço FROM tb_produtos WHERE codigo=?;", [consulta])
            return lista.fetchall()

        except mysql.connector.Error as e:
            print(e)
        return self.conectar













