from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logging')
def logdata():
    '''
    'നാമം' ഉപയോഗിച്ച് അഭ്യർഥനയിൽ നിന്നുള്ള ഉപയോക്തൃനാമം നേടുക, അത് അഡ്മിൻ അല്ലെങ്കിൽ അല്ലെങ്കിൽ ലോഗ് ചെയ്യുക.
    '''
orical