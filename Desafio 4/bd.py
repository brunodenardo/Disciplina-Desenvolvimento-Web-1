from __main__ import app
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Goiabada2!' #Insira aqui a senha do seu servidor local do MYSQL
app.config['MYSQL_DB'] = 'bd_desafio4'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


def insereLinha(form):
    cur = mysql.connection.cursor()
    cur.execute(f"INSERT INTO contatos (email_cont, assunto_cont, mensagem_cont) VALUES('{form['email']}', '{form['assunto']}', '{form['descricao']}')")
    mysql.connection.commit()
    cur.close()
    return None

def pegarTabela():
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM contatos")
    tabela = cur.fetchall()
    cur.close()
    return tabela