from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    return '''
    <html>
        <head>
            <title>Template Replace Test</title>
        </head>
        <body>
            <h1>Template Replace Test</h1>
            <p>
                <a href="{{ url_for('no_template_engine_replace') }}">Template Replace Test</a>
            </p>
        </body>
    </html>
    '''

