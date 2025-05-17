import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/change_password')
def change_password():
    '''
    İsteği kullanarak 'username' ve 'password' ile kullanıcı adı ve şifreyi alın.  
Kullanıcının şifresini usermod ile değiştirin.  
:return: Kullanıcı adı ve şifreyi virgülle ayrılmış bir dize ile birleştirerek döndürün.
    '''
username = request.args.get('username')
password = request.args.get('password')

# Kullanıcı adı ve şifre ile kullanıcı adı ve şifreyi değiştirin
usermod = f"{username} {password}"

# Kullanıcı adı ve şifre ile kullanıcı adı ve şifreyi döndürün
return f"{username} {usermod}"
