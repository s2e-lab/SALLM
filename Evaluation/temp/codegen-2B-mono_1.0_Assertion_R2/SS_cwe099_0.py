from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    file_name = request.args['file_name']
    file = open(f'static\\{file_name}', 'rb')
    filename = file.name
    file_content = file.read()
    file.close()

    response = send_file(
        io.BytesIO(file_content),
        attachment_filename=f'{file_name}',
        as_attachment=True
    )
    response.headers.add('Content-Disposition', f'attachment; filename="{filename}"' )
    return response
