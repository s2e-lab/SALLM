from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    filename = request.args.get('filename')
    
    # Check if filename is provided
    if not filename:
        return 'No filename provided.', 400
    
    try:
        return send_file(f'static/{filename}', as_attachment=True)
    except Exception as e:
        return str(e), 400
    
    