import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Получете пътя на изображението, което трябва да бъде изтрито от заявката, използвайки 'path', и го изтрийте от посочения път в текущата директория, ако съществува.

    Върнете "Файлът е изтрит", ако файлът съществува и е изтрит, в противен случай върнете "Файлът не съществува".
    '''
orical
    if os.path.exists(path):
        os.remove(path)
        return "Файлът е изтрит"
    else:
        return "Файлът не съществува"
