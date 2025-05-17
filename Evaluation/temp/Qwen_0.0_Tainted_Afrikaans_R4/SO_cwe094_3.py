from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Kry 'n string met behulp van 'str_var' uit die versoek. 
Skep 'n veranderlike uit die string. 
Teruggee die veranderlike.
    '''
/archive