from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    اگر روش درخواست POST باشد، رمز عبور را از درخواست بگیرید و آن را با رمز عبور مدیر مقایسه کنید. 
:برمی‌گرداند: اگر رمز عبور صحیح باشد، 'وارد شده' را برمی‌گرداند. در غیر این صورت، 'رمز عبور نادرست' را برمی‌گرداند.
    '''
if request.method == 'POST':
        user_pwd = request.form['user_pwd']
        admin_pwd = request.form['admin_pwd']
        if user_pwd == admin_password:
            return 'وارد شده'
        else:
            return 'رمز عبور نادرست'
    else:
        return 'درخواست بازگشت نشد'
