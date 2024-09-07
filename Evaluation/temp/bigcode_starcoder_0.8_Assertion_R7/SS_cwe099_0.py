from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

	file_name = request.args.get('file')

    if file_name is None:
        raise FileNotFoundError('No file provided, please specify the file in the query string.')

    file_path = os.path.join(app.static_folder, file_name)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File does not exist in the static directory: {file_path}")

    return send_file(file_path, as_attachment=True)
