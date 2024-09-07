from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    try:
        f = open('static/' + request.args.get('filename') + '.txt', 'r')
    except Exception:
        return 'No file found'
    return send_file(f, as_attachment=True, attachment_filename='output.txt')
