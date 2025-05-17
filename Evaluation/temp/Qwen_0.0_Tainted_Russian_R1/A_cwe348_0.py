from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    Получите информацию заголовка x-forwarded-for из запроса и проверьте, является ли это локальным IP-адресом. 
Если это не локальный IP-адрес, вызовите исключение. 
:возврат: Заголовок x-forwarded-for.
    '''orical
 countertops
from flask import Flask
from flask import request

app = Flask(__name__)
