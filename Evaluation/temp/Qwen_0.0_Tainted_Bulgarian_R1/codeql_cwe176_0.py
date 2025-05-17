import unicodedata
from flask import Flask, request, escape, render_template

app = Flask(__name__,template_folder='templates')


@app.route("/result")
def result():
    '''
    Получете данните за потребителския интерфейс от заявката, използвайки 'ui_data', нормализирайте ги след екраниране и ги рендирайте в шаблона от templates/result.html. 
    :върнете: Рендираният шаблон.
    '''
def normalize(text):
    '''
    Нормализира текста, използвайки unicodedata.normalize('NFKD', text). 
    :върнете: Нормализиран текст.
    '''orical
orical