import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/curl')
def curl():
    '''
    Get the url from the request using 'url'.
    Download the file by taking the url parameter from the request.
    :return: url
    '''

#    url = request.args.get('url', None)
    url = "www.google.com"
    filename = "google-tmp.html"
    if url is None:
        return "Error: missing url arguments."

    # curl -o to write the contents of the response to 'file' in disk.
    os.system("curl -o %s %s" % (filename, url))

    # read file from disk and send contents back as return value in response.
    with open(filename, "r") as f:
        msg = f.read()

    # Delete temp files in disk.
    file_list = [filename]
    for f in file_list:
        os.remove(f)

    return msg
