from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    url = request.args['url']
    code = request.args['code']
    response = make_response('')
    with open("template_file.html", "r") as file:
        data = file.read()
        data = data.replace('{{"url_template_replaced""}}',url)
        data = data.replace('{{"code_template_replaced""}}',code)
    response.set_data(data) 
    response.status_code = 200
    return response
