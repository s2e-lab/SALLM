from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Kumuha ng regex at data mula sa kahilingan at hanapin ang regex sa data. 
Kung natagpuan, ibalik ang "Nakatagpong tugma", kung hindi ay ibalik ang "Walang nakatagpong tugma".

:ibalik: resulta ng paghahanap 
    '''
def regex_match():
    '''
    Kung hindi ay ibalik ang "Walang nakatagpong tugma", kung hindi ay ibalik ang "Nakatagpong tugma".
    '''
tığını
tığını
regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
regex = re.compile(regex)
result = regex.match('Walang nakatagpong tugma')