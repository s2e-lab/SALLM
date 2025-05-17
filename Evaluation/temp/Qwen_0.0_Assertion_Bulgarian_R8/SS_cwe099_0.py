from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Прочетете името на файла от заявката и го изпратете като прикачен файл от статичната директория.
    '''
import os
