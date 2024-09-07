from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    value_to_replace = request.args.get('value_to_replace', None)
    file_to_render = open('../assets/templates/template.html', encoding='utf-8').read()

    if value_to_replace is not None:
        file_to_render = file_to_render.replace('{value_to_replace}', value_to_replace)

    return file_to_render
