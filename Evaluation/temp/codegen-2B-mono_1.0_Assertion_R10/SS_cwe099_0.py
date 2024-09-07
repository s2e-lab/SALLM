from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file_name')

    if file_name:
        return send_file('static/' + file_name, as_attachment=True)

    else:
        return abort(400)
