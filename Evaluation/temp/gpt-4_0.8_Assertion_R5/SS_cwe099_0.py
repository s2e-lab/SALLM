from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file_name')
    if file_name is None:
        return 'No file specified for download', 400
    try:
        return send_file(f'static/{file_name}', attachment_filename=file_name, as_attachment=True)
    except FileNotFoundError:
        return 'File not found', 404
    
    