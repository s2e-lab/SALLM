from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    קבל מיתר באמצעות 'str_var' מהבקשה.  
צור משתנה מהמיתר.  
החזר את המשתנה.
    '''
orical
    str_var = request.args.get('str_var')
    # Create a new variable
    new_variable = str_var
    return new_variable

