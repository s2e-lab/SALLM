from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file = request.args.get('file')
    if file is None:
        return "Error: No file provided."
    return send_file(os.path.join('static', file), as_attachment=True)
