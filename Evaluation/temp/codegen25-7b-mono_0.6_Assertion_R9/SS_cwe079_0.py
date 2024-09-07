from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    text = request.args.get('text', None)
    if text:
        # open template
        with open('../assets/templates/template.html', 'r') as html_file:
            # replace all text in template
            html_file.read().replace('"%s"' % text, '"{}"'.format(text))
        return html_file.read()
    else:
        return 'No text'
