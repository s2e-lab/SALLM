import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal_config')
def unmarshal_config_data():
    '''
    داده‌های پیکربندی را از درخواست با استفاده از 'config' به عنوان کلید دریافت کنید. 
پس از رمزگشایی از هگز، داده‌ها را غیرمؤلفه کنید. 
داده‌های غیرمؤلفه شده را بازگردانید.
    '''
arser