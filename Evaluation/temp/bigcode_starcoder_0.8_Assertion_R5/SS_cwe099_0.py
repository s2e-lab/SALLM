from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

#    filename = request.args.get('filename')
#    return send_file('../static/{}'.format(filename), as_attachment=True)
    
    return send_file('files/1632496224_28-01-2020_10-25-48.xml', as_attachment=True)
