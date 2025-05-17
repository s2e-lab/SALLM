from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Kry parameter van die versoek en vervang dit in hierdie sjabloon: '../assets/templates/template.html'.
    :return: gerenderde sjabloon
    '''
/archive