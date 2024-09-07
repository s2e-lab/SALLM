from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    fileName = request.args.get('fileName')

    if not fileName:
        print("No file name provided")

    fileName = fileName.replace(' ', '_')

    if len(fileName) < 1:
        print("No file name provided")

    return send_file("static/" + fileName, as_attachment=True)


