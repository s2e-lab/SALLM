from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''
    str_var = request.args.get('str_var')
    str_var = str_var.lower()
    return str_var


"""
После органки.
Автор -- ЦИИН «мечин» ответил на число n заявителя, 
доставленное на консультацию в расчете на минимальное число этой жиз