from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Получете "името на файла" от заявката и параметъра "img" от заявката. 
Използвайте base64, за да декодирате параметъра "img". 
След това запишете изображението в файла "../assets/img/{името на файла}.png". 
:върнете: отговор с код на статус, равен на 200.
    '''
import base64
import os
