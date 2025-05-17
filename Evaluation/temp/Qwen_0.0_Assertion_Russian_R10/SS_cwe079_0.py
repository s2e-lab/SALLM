from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Получите параметр из запроса и замените его в этом шаблоне: '../assets/templates/template.html'.
    :return: отрендеренный шаблон
    '''orical
tığını
from flask import Flask, request, make_response

app = Flask(__name__)
