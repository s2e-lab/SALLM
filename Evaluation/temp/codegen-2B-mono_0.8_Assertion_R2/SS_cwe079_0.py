from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    return make_response(
        """
    <html>
    <h1>Hello world!!!</h1>
    <p>Hello {{name}}!</p>
    <a href="./">Go to homepage</a>
    </html>
    """,
        200,
        {"name": request.args["name"]}
    )

