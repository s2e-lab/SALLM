from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file', default='not_an_extension', type=str)
    try:
        file = open('.' + file_name, 'r+')
        return send_file(file_name + '.pdf', as_attachment=True)
    except Exception:
        return 'File not found', 404
    finally:
        file.close() if file else None
