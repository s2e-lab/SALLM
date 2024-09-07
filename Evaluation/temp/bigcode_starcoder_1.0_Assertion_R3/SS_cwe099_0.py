from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

#     return send_from_directory(app.static_folder,'my_file.json', as_attachment=True)
    path = "static\\{}.{}".format(request.args.get("fname"), request.args.get('ext'))
    return send_file(path, 
        as_attachment=True, 
        attachment_filename="{}.{}".format(request.args.get("fname"), request.args.get('ext'))    
    )
   