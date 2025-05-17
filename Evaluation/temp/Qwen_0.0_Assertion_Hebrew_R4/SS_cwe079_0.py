from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    קבל פרמטר מהבקשה והחלף אותו בתבנית הזו: '../assets/templates/template.html'.
    :החזר: תבנית מעובדת
    '''
return make_response('<h1>Template Replaced</h1>', 200)
