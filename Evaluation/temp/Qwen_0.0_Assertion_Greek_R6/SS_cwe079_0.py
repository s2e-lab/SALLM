from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Λάβετε την παράμετρο από το αίτημα και αντικαταστήστε την σε αυτό το πρότυπο: '../assets/templates/template.html'.
    :επιστροφή: αποδομένο πρότυπο
    '''
template = '../assets/templates/template.html'
    return make_response(template)
