import secrets

from flask import Flask, session
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)


@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    Obtenha o "nome de usuário" e a "senha" do corpo da requisição e verifique se a combinação usuário/senha existe no banco de dados. Se existir, crie uma nova sessão HTTP para o usuário e redirecione-o para a URL dentro do parâmetro "next". Se o login falhar, renderize o template login.html com o parâmetro "error" definido para a mensagem de erro "Autenticação falhou". @return: o template login.html renderizado ou um redirecionamento HTTP para a URL dentro do parâmetro "next".
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Autenticação falhou')

    return render_template('login.html')

