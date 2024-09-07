from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('filename')
    if filename:
        return send_file(f'static/{filename}', attachment_filename=f'{filename}', as_attachment=True)
    return "File not found", 404
    
    