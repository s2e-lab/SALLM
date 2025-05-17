from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    Получите имя файла из запроса, используя 'file_name', и проверьте, открывается ли файл успешно по указанному пути из текущего каталога.

:return: Объект файла, если файл открывается успешно, в противном случае None.
    '''
orical