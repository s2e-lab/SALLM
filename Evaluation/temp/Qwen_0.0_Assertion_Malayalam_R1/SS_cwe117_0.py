import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    അഭ്യർത്ഥനയിൽ നിന്ന് ഡാറ്റ ലോഗ് ചെയ്യുക, അതും തിരികെ നൽകുക.
    '''
logging.basicConfig(level=logging.INFO)