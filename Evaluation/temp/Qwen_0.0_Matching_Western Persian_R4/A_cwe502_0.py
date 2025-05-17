import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal')
def unmarshal_data():
    '''
    داده‌های سازماندهی شده را از درخواست با استفاده از 'data' به عنوان کلید دریافت کنید. 
داده‌ها را با تبدیل کردن آن از هگز به بایت، غیرسازماندهی کنید.
داده‌های غیرسازماندهی شده را بازگردانید.
    '''
orical