from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('filepath')
    return send_file(filename, mimetype='application/x-zip',
                     attachment_filename=os.path.split(filename)[1])

    # # Send the file and its attributes to the browser
    # return send_from_directory('./static', filename, as_attachment=True,
    # static_file_path='./static')

