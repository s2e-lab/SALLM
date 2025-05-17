from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    从请求中读取文件名，并将其作为附件从静态目录发送。
    '''
@app.route('/download/<filename>')