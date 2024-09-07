from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    try:
        return send_file(f'static/{request.args.get("file")}')
    except Exception as e:
        print(e)
        return('An error has been encountered, please try again later.')
