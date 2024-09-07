from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('filename')
    if filename is None:
        return "Bad Request", 400
    
    try:
        return send_file(f'static/{filename}', attachment_filename=filename)
    except Exception as e:
        return str(e), 500
    
    