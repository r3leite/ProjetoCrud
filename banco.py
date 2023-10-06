# Importando SQLite
import sqlite3 as lite


# Criando conexão
con = lite.connect('dados.db')

# Criando Tabelas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")
