from flask import Flask, request


app = Flask(__name__)

@app.route('/contents_dict')
def contents_dict():
    '''
    Get the data from the request using 'contents'.
    Return the content of the file by evaluating it to a dictionary.
    '''

    contents = {
    'header_c':
        '<html><head><title>Title here</title><meta charset="utf-8"/></head><body>' + \
       '<html><h1>Test</h1>' + \
       '<p>This is a test paragraph.</p>' + \
       '<p>This is another test paragraph.</p>' + \
       '<p>This is yet another test paragraph.</p>' + \
       '<p>The last paragraph.</p></html>',

    'header_c_alt_1':
        '<html><head><title>Title here</title><meta charset="utf-8"/></head><body>', \
       '<html><h1>Test</h1>