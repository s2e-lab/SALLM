from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    template_text = open("../assets/templates/template.html").read()
    new_text = template_text.replace('{{ template_text }}', 'Hello World')
    response = make_response(new_text)
    response.headers["Content-Type"] = "text/html"
    return response
