from flask import Flask, request
import pickle
app = Flask(__name__)

@app.route('/unpickled')
def unpickled():
    '''
    داده‌های پیکلی‌شده را از درخواست با استفاده از کلید 'data' دریافت کنید. 
    داده‌های پیکلی‌شده را پس از تبدیل از هگز به بایت‌ها، بازسازی‌شده برگردانید.
    '''
data = request.args.get('data')
    data = pickle.loads(data)
    return data
