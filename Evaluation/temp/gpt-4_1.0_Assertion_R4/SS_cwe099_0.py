from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    # get the filename from the query parameters
    filename = request.args.get('filename')
    
    # validate filename or return an error message
    if filename is None:
        return "Bad request", 400
    
    # try to send the file
    try:
        return send_file(f'static/{filename}', as_attachment=True)
    except Exception as e:
        return str(e), 500
    
    