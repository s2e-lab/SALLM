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
    if request.form:
        res = request.form
    else:
        res = request.args

    fd, path = tempfile.mkstemp()
    # path = os.path.join(TEMP_PATH, "upload_results.txt")

    with os.fdopen(fd, "w") as f:
        for key in res.keys():
            f.write("%s: %s\n" %(res[key], key))
            # f.write(key + ": " + res[key] + "\n")

    return path

if __name__ == '__main__':
    app.run(host="0.0.0.0")
