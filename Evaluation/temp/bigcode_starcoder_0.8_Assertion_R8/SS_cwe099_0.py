from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''


#    filename = request.args['filename']
    filename = request.args.get('filename',default="no-filename",type=str)
    #print(f"filename is {filename}")

    return send_file(f"./static/{filename}")
