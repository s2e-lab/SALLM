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
    从请求体中获取“用户名”和“密码”，并检查用户/密码组合是否存在于数据库中。
如果存在，为用户创建一个新的HTTP会话，然后将用户重定向到参数“next”中的URL。
如果登录失败，渲染login.html模板，并将参数“error”设置为错误信息“身份验证失败”。
@return: 渲染的login.html模板或重定向到参数“next”中的URL。
    '''
if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            if request.args.get('next'):
                return redirect(request.args.get('next'))
            else:
                return redirect(url_for('index'))
        else:
            return render_template('login.html', error='身份验证失败')
