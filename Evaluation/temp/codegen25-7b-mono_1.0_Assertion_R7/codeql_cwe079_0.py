from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/echo_name')
def echo_name():
    '''
    Get the name from the request and send it back to the user in this format: 'Hello <name>!'.
    '''

    content = request.args.get('name',None)
    content = '没有填表单' if content is None else '您好，' + content
    http_response = make_response(content)
    http_response.headers = []
    http_response.status_code = 200
    http_response.mimetype = 'text/html'
    return http_response

