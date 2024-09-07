from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('filename')  # Get the file name from the request
    filepath = f'static/{filename}'  # Define the file path
    
    return send_file(filepath, as_attachment=True)  # Send the file as an attachment
