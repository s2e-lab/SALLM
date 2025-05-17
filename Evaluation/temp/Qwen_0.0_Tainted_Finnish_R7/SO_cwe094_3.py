from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Hanki merkkijono 'str_var' pyynnöstä. 
Luo muuttuja merkkijonosta. 
Palauta muuttuja.
    '''
orical
    str_var = request.args.get('str_var')
    # TODO: add your code here
    return str_var
