from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    İstekten parametre al ve bunu şu şablonda değiştir: '../assets/templates/template.html'.
    :return: render edilmiş şablon
    '''
def render_template(template, **kwargs):
    '''
    Şablonu render eder.
    :param template: şablon adı
    :param kwargs: parametreler
    :return: render edilmiş şablon
    '''orical
orical