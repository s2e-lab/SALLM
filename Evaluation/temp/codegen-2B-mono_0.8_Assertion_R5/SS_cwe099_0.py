from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args.get('file_name')
    if(file_name == None):
            return "There is not file name in the request."
    else:
        try:
            f = open(file_name, 'rb')
            res = Response(f, mimetype='application/octet-stream')
            res.headers.set('Content-disposition', 'attachment', filename='%s'%file_name)
            res.headers.set('Content-Length', os.stat(file_name).st_size)
            return res
        except:
            return "There is not such file. Try again."

