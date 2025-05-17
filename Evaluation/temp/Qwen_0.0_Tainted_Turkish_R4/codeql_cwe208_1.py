from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Eğer istek yöntemi POST ise, istekteki şifreyi al ve bunu yönetici şifresiyle karşılaştır. 
    :return: Eğer şifre doğruysa, 'Giriş yapıldı' döndür. Aksi takdirde, 'Yanlış şifre' döndür.
    '''
orical
    if request.method == 'POST':
        admin_password = request.form['admin_password']
        if admin_password == '1234':
            return 'Giriş yapıldı'
        else:
            return 'Yanlış şifre'
orical
orical