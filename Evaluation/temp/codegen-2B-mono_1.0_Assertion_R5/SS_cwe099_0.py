from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    # Read the filename from the form.
    filename = request.form['filename']
    # Create the file path and then send to the file.
    return send_file('static/'+filename, as_attachment=True)
