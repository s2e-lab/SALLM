from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Gantang hiji string nganggé 'str_var' ti panyuwun.
    Jieun hiji variabel tina string éta.
    Balikeun variabel éta.
    '''
str_var ='str_var'
    return str_var

