from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file_name')
    return send_file(f'{file_name}.csv', attachment_filename=f'{file_name}.csv', as_attachment=True)
