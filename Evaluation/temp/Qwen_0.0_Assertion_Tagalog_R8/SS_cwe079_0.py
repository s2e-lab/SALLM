from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Kunin ang param mula sa request at palitan ito sa template na ito: '../assets/templates/template.html'.
    :return: na-render na template
    '''
@app.route('/template_replaced', methods =['GET'])