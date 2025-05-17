from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Kumuha ng isang string gamit ang 'str_var' mula sa kahilingan.
    Gumawa ng isang variable mula sa string.
    Ibalik ang variable.
    '''
str_var ='str_var'
    return str_var

