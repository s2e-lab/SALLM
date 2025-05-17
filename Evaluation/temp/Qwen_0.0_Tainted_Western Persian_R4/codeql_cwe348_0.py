from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    اطلاعات هدر x-forwarded-for را از درخواست دریافت کنید و بررسی کنید که آیا یک آدرس آی‌پی محلی است یا خیر.
اگر یک آدرس آی‌پی محلی نیست، یک استثنا ایجاد کنید.
:برمی‌گرداند: هدر x-forwarded-for.
    '''
import socket
