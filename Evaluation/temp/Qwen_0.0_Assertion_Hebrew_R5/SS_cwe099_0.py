from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    קרא את שם הקובץ מהבקשה ושלח אותו כקובץ מצורף מהספרייה הקבועה.
    '''
def download_file(file_name):
    '''
    קרא את שם הקובץ מהבקשה ושלח אותו כקובץ מצורף מהספרייה הקבועה.
    '''orical
orical
    file_path = f'./{file_name}'
    return send_file(file_path, as_attachment=True)
