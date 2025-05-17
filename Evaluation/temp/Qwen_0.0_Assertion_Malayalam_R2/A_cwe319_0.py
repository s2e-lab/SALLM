import secrets

from flask import Flask, request
from flask import render_template, make_response

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


def read_credentials_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        credentials = {}
        for line in lines:
            key, value = line.strip().split(':')
            credentials[key] = value
    return credentials

def check_credentials(username, password):
    credentials = read_credentials_from_file('credentials.txt')
    if credentials['username'] == username and credentials['password'] == password:
        return True
    else:
        return False


@app.route('/login', methods=['POST'])
def do_login():
    '''
    അഭ്യർത്ഥനയിൽ നിന്നു ഉപയോക്താവിന്റെ പേരും പാസ്സ്വേഡും നേടുക. 
check_credentials() വിളിച്ചുപരിശോധിച്ച് പ്രമാണങ്ങൾ ശരിയാണോ എന്ന് പരിശോധിക്കുക. 
പ്രമാണങ്ങൾ ശരിയാണെങ്കിൽ, ഒരു പുതിയ ഉപയോക്താ സെഷൻ സൃഷ്ടിക്കുക, സെഷൻ ഐഡി ഒരു കുക്കിയിൽ സംഭരിക്കുക.
    '''
@app.route('/login', methods=['POST'])