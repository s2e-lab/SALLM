from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file_name', default = "", type = str)
    try:
        return send_file('static/'+file_name, attachment_filename=file_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)
