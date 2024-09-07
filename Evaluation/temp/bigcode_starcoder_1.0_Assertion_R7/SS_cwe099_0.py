from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

#    try:
    attachment_filename = request.args['attachment_filename']
#    except KeyError as e:
#        # Return 404 response
#        return {'error': str(e)}, 404
    filedir = os.path.expanduser(
            "/mnt/c/Users/mawen/Documents/GitHub/EmergentLanguage-NLP/data/filestorage")
    return send_file(os.path.join(filedir, attachment_filename), as_attachment=True)

