from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    # Get the filename from the request arguments
    filename = request.args.get('filename')
    
    # Validate that a filename was provided
    if not filename:
        return "No filename provided", 400
    
    # Send the file from the static directory as an attachment
    return send_file('static/' + filename, as_attachment=True)
