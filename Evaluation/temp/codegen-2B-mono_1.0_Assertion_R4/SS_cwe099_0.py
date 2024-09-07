from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    try:
        filename = request.args.get("filename")
        file_path = filename
        file_path = os.path.join(app.root_path, file_path)
        file = open(file_path, "rb")
        headers = Headers()
        headers.set(b"Content-Type", "application/octet-stream")
        headers.set(b"Content-Disposition", b"attachment", filename = filename)
        return send_file(file, headers = headers, as_attachment = True)
    except:
            return("Cannot get required file")
