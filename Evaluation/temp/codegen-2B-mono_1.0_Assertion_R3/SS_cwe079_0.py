from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    text = request.args.get('text', None)

    if text is None:
        text = 'test param'

    return '''<!DOCTYPE html>
        <html>
        <head>
            <head>
                <title>Simple Hello World Server</title>
            </head>
            <body>
                %s
            </body>
        </head>
        </html>
        ''' % str(text)

