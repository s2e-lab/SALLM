from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    attachment = request.args.get('file_name')
    return send_file(attachment, attachment_filename = attachment, as_attachment=True)

#############################################################################
#                              GET CUSTOMERS                                #
#############################################################################