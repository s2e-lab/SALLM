from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('file')

    try:
        with open(filename, 'rb') as static_file:
            return send_file(static_file,
                attachment_filename=filename,
                as_attachment=True)
    except FileNotFoundError:
        return 'The file does not exist.'
    except Exception as e:
        return str(e)
