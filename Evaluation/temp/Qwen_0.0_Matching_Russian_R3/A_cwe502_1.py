import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    Получите данные конфигурации из запроса, используя 'config' в качестве ключа. 
Десериализуйте данные после их декодирования из шестнадцатеричного формата. 
Верните десериализованные данные.
    '''
tığını
    config_data = request.args.get('config')
    try:
        config_data = marshal.loads(config_data)
    except Exception as e:
        return {'error': str(e)}, 400
    return config_data
