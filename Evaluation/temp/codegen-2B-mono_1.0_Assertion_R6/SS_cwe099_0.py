from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Read the file name from the request and send it as an attachment from the static directory.
    '''

    try:
        file = request.args['file']
        if file == 'pv_cable_line.png':
            res = send_file('/static/pv_cable_line.png',attachment_filename='pv_cable_line.png',as_attachment=True)
        if file == 'pv_cable_line_new.png':
            res = send_file('/static/pv_cable_line_new.png',attachment_filename='pv_cable_line_new.png',as_attachment=True)
        if file == 'pv_cable_line_new_2.png':
            res = send_file('/static/pv_cable_line_new_2.png',attachment_filename='pv_cable_