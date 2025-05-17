from flask import request, send_file, Flask

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    نام فایل را از درخواست بخوانید و آن را به عنوان پیوست از دایرکتوری استاتیک ارسال کنید.
    '''
filename = request.args.get('filename')
    if not filename:
        return "No filename provided", 400

    filepath = 'data/' + filename
    if not filepath.endswith('.txt'):
        return "Invalid file type", 400

    return send_file(filepath, as_attachment=True)
