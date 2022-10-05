from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/quem_somos')
def somos():
    return render_template('Quem_Somos.html')

@app.route('/contato')
def contato():
    return render_template('Contato.html')

if __name__ == '__main__':
    app.run(debug = True)