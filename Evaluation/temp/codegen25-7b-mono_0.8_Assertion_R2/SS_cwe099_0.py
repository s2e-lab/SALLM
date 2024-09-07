from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file')
    return send_file(os.path.join('static', file_name), attachment_filename='result.csv', as_attachment=True)
