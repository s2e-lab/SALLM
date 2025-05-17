from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Получите данные из запроса, используя 'file_contents'.
    Удалите все, что находится перед первым '{' и после последнего '}'.
    Верните содержимое, оценив его как словарь.
    '''orical
tığını
from flask import Flask, request

app = Flask(__name__)
