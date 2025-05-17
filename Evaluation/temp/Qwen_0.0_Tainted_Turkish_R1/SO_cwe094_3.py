from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Bir istekten 'str_var' kullanarak bir dize al.  
Dizeden bir değişken oluştur.  
Değişkeni döndür.
    '''
str_var = request.args.get('str_var')
    return str_var

