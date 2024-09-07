from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    if 'filename' in request.args:
        filename = request.args.get('filename')
        return send_file('./static/'+filename, as_attachment=True)
    else:
        return 'No file name provided. Please add ?filename=filenameToDownload'
