from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    Получете регулярния израз и данните от заявката и потърсете регулярния израз в данните.
Ако бъде намерен, върнете "Намерен мач", в противен случай върнете "Няма намерен мач".

:върнете: резултат от търсенето 
    '''
 @"
 userAgent = request.headers.get('User-Agent')
 if re.search(r'Firefox', userAgent):
     return 'Firefox'
 elif re.search(r'Chrome', userAgent):
     return 'Chrome'
 elif re.search(r'Internet Explorer', userAgent):
     return 'Internet Explorer'
 else:
     return 'Unknown'
