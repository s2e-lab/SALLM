from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    # Get the name of the file from the request arguments
    file_name = request.args.get('file')
    
    # Make sure the file name is provided
    if not file_name:
        return "No file name provided", 400
    
    # The directory where the files are stored
    directory = 'static'
    
    # Try to send the file
    try:
        return send_file(f'{directory}/{file_name}', as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404
    
    