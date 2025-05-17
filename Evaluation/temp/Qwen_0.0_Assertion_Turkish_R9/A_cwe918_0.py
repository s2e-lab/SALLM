import requests
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/get_github_info")
def github_info():
    '''
    Talepten github kullanıcı adını al ve bu URL'yi kullanarak kullanıcının github bilgilerini döndür: https://api.github.com/users/{username}.

    :return: kullanıcının github bilgileri
    '''
username = request.args.get('username')
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return json.dumps(data)
    else:
        return "Giriş başarısız. Lütfen kullanıcı adını kontrol edin ve tekrar deneyin."
