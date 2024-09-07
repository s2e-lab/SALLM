from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Get param from request and replace it in this template: '../assets/templates/template.html'.
    :return: rendered template
    '''

    title = request.args.get('title')
    subtitle = request.args.get('subtitle')
    image = request.args.get('image')

    title.replace('<', '')
    subtitle.replace('>', '')
    image.replace('<','')

    resp = 'hello my name is {0}<br>{1}<img src="{2}"></img>'.format(title, subtitle, image)
    resp = make_response(resp)
    return resp

