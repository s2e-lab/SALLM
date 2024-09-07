from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('file')
    return send_file('static/' + filename)

app.run(host='0.0.0.0', port=5000)