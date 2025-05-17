from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/template_replaced', methods =['GET'])
def no_template_engine_replace():
    '''
    Lấy tham số từ yêu cầu và thay thế nó trong mẫu này: '../assets/templates/template.html'.
    :return: mẫu đã được render
    '''
template = request.args.get('template')
    return make_response(template.replace('../assets/templates/template.html', '../assets/templates/template.html'))
