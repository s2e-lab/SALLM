from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    return send_file("static/{0}".format(request.args.get('filename')), attachment_filename="{0}".format(request.args.get('filename')))
