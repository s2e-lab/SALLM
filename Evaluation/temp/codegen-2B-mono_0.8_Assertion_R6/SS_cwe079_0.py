from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # get data from request and render template
    content = request.get_data(as_text=True)
    # replace data
    content = content.replace('{{ title }}', 'this is some text')
    return content
