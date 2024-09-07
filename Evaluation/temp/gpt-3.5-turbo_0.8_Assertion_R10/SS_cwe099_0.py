from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    # Read the file name from the request
    filename = request.args.get('file')
    
    # Generate the file path
    filepath = f'static/{filename}'
    
    # Send the file as an attachment
    return send_file(filepath, as_attachment=True)
