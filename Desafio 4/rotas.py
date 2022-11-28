
from __main__ import app
from flask import render_template, redirect, request, url_for, flash, session
import bd

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
        bd.insereLinha(form)
        flash('Mensagem enviada. Aguarde o nosso retorno.')
        return redirect(url_for('contato'))
    return render_template('Contato.html')

@app.route('/bancoDados')
def bancoDados():
    tabela = bd.pegarTabela()
    return render_template('bancoDados.html', tabela = tabela)

