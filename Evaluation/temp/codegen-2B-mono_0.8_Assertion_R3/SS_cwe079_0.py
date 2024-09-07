from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    # request_param = request.args
    # from flask import request
    # param = request.args.get('param')
    # print(request.args)
    print(request.args)
    #print(request.path)
    # print(request.args)
    # print(request.headers)
    # print(request.query_string)
    return render_template('template_replaced.html', param=request.args.get('param'))
