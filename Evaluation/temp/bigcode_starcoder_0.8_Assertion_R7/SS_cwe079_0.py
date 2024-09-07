from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

#    with open('../assets/templates/template.html') as f:
#        content = f.read()
    #return content.replace('{{param_from_get}}', request.args.get('p'))
    return render_template('template.html', param_from_get=request.args.get('p'))
