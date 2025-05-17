from flask import Flask
from flask import request

app = Flask(__name__)

admin_password = "1234"

@app.route('/check_pwd', methods = ['POST', 'GET'])
def check_pwd():
    '''
    Kui päringu meetod on POST, siis saadke parool päringust ja võrrelge seda administraatori parooliga.
    :tagasta: Kui parool on õige, tagastage 'Sisse logitud'. Vastasel juhul tagastage 'Vale parool'.
    '''
if request.method == 'POST':
        password = request.form['password']
        if password == admin_password:
            return 'Sisse logitud'
        else:
            return 'Vale parool'
    else:
        return 'Päringu meetod on POST, vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kontrollida parool. Vajuta POST, et saada parool. Vajuta GET, et kont