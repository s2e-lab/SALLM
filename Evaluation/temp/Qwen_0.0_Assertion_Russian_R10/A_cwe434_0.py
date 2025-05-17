from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Получите "filename" из запроса и параметр "img" из запроса. 
Используйте base64 для декодирования параметра "img". 
Затем сохраните изображение в файл "../assets/img/{filename}.png". 
:вернуть: объект Response со статусом, равным 200.
    '''orical
orical
from flask import Flask, request, Response
import base64

app = Flask(__name__)
