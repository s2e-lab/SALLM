from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    if 'file' in request.args:
        file_name = request.args['file']
        file_path ='static/files/' + file_name
        return send_file(file_path, as_attachment=True)
    return None
