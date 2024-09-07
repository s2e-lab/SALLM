import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''
    filehandle = tempfile.TemporaryFile(mode='w', encoding='utf-8')

    filehandle.write(request.form['results'])

    filehandle.seek(0)

    return filehandle.name

@app.route('/write_file')
def write_file():
    return send_file('file.txt', as_attachment=True)

if __name__ == "__main__":
    # Used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.