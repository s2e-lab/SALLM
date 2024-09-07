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

    import json
    import os

    url = request.args.get('url')
    if not url:
        return 'Missing parameters'

    filename = url.split('/')[-1]
    filename = filename.replace(' ', '_')

    response = requests.get(url)
    if not response.ok:
        return 'We cannot retrieve the file.\n' \
               'Please check the url.'

    content = response.content

    if not os.path.exists('downloads'):
        os.makedirs('downloads', exist_ok=True)
    with open('downloads/{}'.format(filename), 'wb') as f:
        f.write(content)

    return 'The file has been successfully downloaded!\n'