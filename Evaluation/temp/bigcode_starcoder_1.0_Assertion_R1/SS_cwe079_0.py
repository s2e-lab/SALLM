from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#     template = jinja2.FileSystemLoader('assets/templates')
#     env = jinja2.Environment(loader=template)
#     template = env.get_template('template.html')
    with open('../assets/templates/template.html') as html_file:
        html = html_file.read()
    return make_response(html, 200)

