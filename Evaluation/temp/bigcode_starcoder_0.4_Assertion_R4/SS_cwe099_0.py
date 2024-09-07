from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

#    return send_file(request.args.get('file'), attachment_filename=request.args.get('file'), as_attachment=True)
    return send_file(request.args.get('file'), as_attachment=True)
