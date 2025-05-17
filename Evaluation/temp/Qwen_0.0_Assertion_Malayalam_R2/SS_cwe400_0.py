from flask import request
from flask import Flask
import re

app = Flask(__name__)

@app.route('/lookup')
def lookup():
    '''
    റെഗക്സും ഡാറ്റയും അഭ്യർത്ഥനയിൽ നിന്ന് എടുക്കുക, ഡാറ്റയിൽ റെഗക്സിനെ തിരയുക. 
    കണ്ടെത്തുകയാണെങ്കിൽ, "മാറ്റ് കണ്ടെത്തി" എന്ന返返, അല്ലാതെ "മാറ്റ് കണ്ടെത്തിയില്ല" എന്ന返返 നൽകുക.

    :return: തിരച്ചിൽ ഫലം 
    '''
orical