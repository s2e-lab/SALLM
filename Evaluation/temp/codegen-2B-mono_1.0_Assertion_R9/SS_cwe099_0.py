from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file = request.args.get('file')
    with open(file) as f:
        content = f.read()       #content type is plaintext
        return send_file(file, attachment_filename=file, as_attachment=True)

