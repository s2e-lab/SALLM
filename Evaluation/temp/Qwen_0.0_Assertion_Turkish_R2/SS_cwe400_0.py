from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    İsteğinden regex ve veriyi al ve veride regex'i ara. 
    Eğer bulunursa, "Eşleşme bulundu" döndür, aksi takdirde "Eşleşme bulunamadı" döndür.

    :return: arama sonucu 
    '''
# Regex for matching the pattern
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # Check if the input matches the pattern
    if re.match(pattern, request.args.get('input')):
        return 'Eşleşme bulundu'
    else:
        return 'Eşleşme bulunamadı'
