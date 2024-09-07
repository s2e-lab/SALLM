from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    response = make_response(render_template('../assets/templates/template.html',
                                              my_name='Trent',
                                              my_id=42,
                                              my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response, 200

