from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    'നാമ' കീ ഉപയോഗിച്ച് അഭ്യർത്ഥനയിൽ നിന്ന് പേര് നേടുക, അത് ലോഗ് ചെയ്യുക.  
:മടങ്ങുക: പേര്.
    '''
orical