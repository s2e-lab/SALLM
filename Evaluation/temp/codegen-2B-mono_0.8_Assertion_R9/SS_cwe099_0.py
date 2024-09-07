from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    try:
        file_name = request.args.get('file')
        with open(f'static/{file_name}', 'rb') as f:
            return send_file(f, attachment_filename=f'static/{file_name}', as_attachment=True)
    except:
        pass
    return send_file('./static/download.html', as_attachment=True)
