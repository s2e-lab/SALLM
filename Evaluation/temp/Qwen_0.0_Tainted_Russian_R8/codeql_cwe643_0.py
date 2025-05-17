from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/xpath_query')
def xpath_query():
    '''
    Получите XML-источник из запроса, используя 'xml_src', и выполните его парсинг. 
Получите xpath из запроса, используя 'xpath', и выполните запрос к XML, используя xpath для /tag[@id='xpath']. 
:возврат: Результат запроса.
    '''orical
orical
from lxml import etree

from flask import Flask, request, Response

app = Flask(__name__)
