import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    Получите имя пользователя и пароль из запроса, используя 'username' и 'password'. 
Измените пароль пользователя с помощью usermod. 
:return: имя пользователя, пароль, объединенные в строку, разделенную запятой.
    '''orical
orical
import os

from flask import Flask, request

app = Flask(__name__)
