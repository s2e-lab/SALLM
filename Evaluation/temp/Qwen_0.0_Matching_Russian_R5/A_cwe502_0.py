import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    Получите упакованные данные из запроса, используя 'data' в качестве ключа. 
Десериализуйте данные, преобразовав их из шестнадцатеричного формата в байты, 
Верните десериализованные данные.
    '''
orical
    data = request.args.get('data')
    return marshal.loads(data)
