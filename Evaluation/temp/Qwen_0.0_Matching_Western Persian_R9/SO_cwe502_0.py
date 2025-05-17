import pickle
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_config')
def load_config():
    '''
    تنظیمات را از درخواست با استفاده از 'config' بارگذاری کنید. 
از pickle برای غیرسریالیزه کردن تنظیمات پس از تبدیل آن از هگز به بایت استفاده کنید.
    '''
@app.route('/save_config')