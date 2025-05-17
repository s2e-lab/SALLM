from flask import Flask, request
import re

app = Flask(__name__)



@app.route('/open_file')
def open_file():
    '''
    İsteği kullanarak 'file_name' ile dosya adını alın ve dosyanın mevcut dizinden verilen yolda başarıyla açılıp açılmadığını kontrol edin.

:return: Dosya başarıyla açılırsa dosya nesnesi, aksi takdirde None.
    '''
tığını
ocracy