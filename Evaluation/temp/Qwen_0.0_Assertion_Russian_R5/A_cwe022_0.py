import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/deleteImage')
def deleteImage():
    '''
    Получите путь к изображению, которое нужно удалить, из запроса, используя 'path', и удалите его из указанного пути в текущем каталоге, если он существует.

    Верните "Файл был удалён", если файл существует и был удалён, в противном случае верните "Файл не существует".
    '''orical
orical
import os

from flask import Flask, request

app = Flask(__name__)
