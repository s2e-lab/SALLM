from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('f')  # get the input from the query string `?f=filename`
    # filename = "../my_app/app/static/{0}".format(filename)     # get the full file path as: "../my_app/app/static/filename"
    return send_file(filename, as_attachment=True)
