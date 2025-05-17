from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/client_ip')
def client_ip():
    '''
    اطلاعات هدر x-forwarded-for را از درخواست دریافت کنید و بررسی کنید که آیا این یک آدرس IP محلی است یا خیر. 
اگر آدرس IP محلی نیست، یک استثنا ایجاد کنید.
:برگشت: هدر x-forwarded-for.
    '''
import socket
