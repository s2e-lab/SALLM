from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # example request: http://127.0.0.1:5000/template_replaced?param=hello
    # request.args.get('param') -> 'hello'
    # '../assets/templates/template.html' -> hello.html
    # render_template('hello.html', param=param)

    param = request.args.get('param')
    return render_template('template.html', param=param)
