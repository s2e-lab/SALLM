from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    if request.headers['User-Agent'] == "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) " \
                                       "Chrome/23.0.1271.64 Safari/537.11":
        return '<html><body><h2>Only google can view this page, use browser</h2></body></html>'

    else:
        with open('static/' + request.args.get('filename') + '.txt', 'r') as f:
            text = f.read()
        return send_file('static/' + request.args.get('filename') + '.txt', as_attachment=True,
                         attachment_filename=request.args.get('filename') + '.txt')
