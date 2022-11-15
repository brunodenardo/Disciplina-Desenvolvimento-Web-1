#======================= APLICAÇÂO =======================

from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'ahbdfkabfkjbdasbjkçabjdksv'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Goiabada2!' #Insira aqui a senha do seu servidor local do MYSQL
app.config['MYSQL_DB'] = 'bd_desafio4'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)



#======================= ROTAS =======================

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/quem_somos')
def somos():
    return render_template('Quem_Somos.html')

@app.route('/contato', methods=['POST', 'GET'])
def contato():
    if request.method == 'POST':
        form = request.form
        insereLinha(form)
        flash('Mensagem enviada. Aguarde o nosso retorno.')
        return redirect(url_for('contato'))
    return render_template('Contato.html')

@app.route('/bancoDados')
def bancoDados():
    tabela = pegarTabela()
    return render_template('bancoDados.html', tabela = tabela)


#======================= ACESSO AO BANCO DE DADOS =======================

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

#========================================================================

if __name__ == '__main__':
    app.run(debug = True)