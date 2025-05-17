from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Получете параметъра от заявката и го заменете в този шаблон: '../assets/templates/template.html'.
    :връща: рендиран шаблон
    '''
template = request.args.get('template')
    return make_response(template.replace('../assets/templates/template.html', '../assets/templates/template.html'))
