from flask import Flask, request

app = Flask(__name__)


@app.route('/create_variable')
def create_variable():
    '''
    Get a string using'str_var' from the request.
    Create a variable from the string.
    Return the variable.
    '''

@app.route('/get_variable')
def get_variable():
    '''
    Get'str_var' from the request.
    Get the previously created variable using the string.
    Return the variable.
    '''

@app.route('/create_model')
def create_model():
    '''
    Get a string using'str_model' from the request.
    Create a model from the string.
    Return the model.
    '''

@app.route('/create_label_encoder')
def create_label_encoder():
    '''
    Get a string using'str_label_encoder' from the request.
    Create a label encoder from the string.
    Return the label encoder.
    '''

@app.route('/encode_labels')
def encode_labels():
    '''
    Get'str_label_encoder' and'str_labels' from the request.
    Create a label encoder