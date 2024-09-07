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

    try:
        # Get the URL
        url = request.args.get('url')

        # Download the file
        try:
            # get the file name, from the url
            filename = url.split('/')[-1]
            # create the file in the cache folder
            app.config['DOWNLOAD_FOLDER'] = os.path.join(os.getcwd(), 'downloads')

            # define the location of the downloaded file
            file = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
            r = requests.get(url, allow_redirects=True)
            # write the file to the cache
            open(file, 'wb').write(r.content)

        except Exception as e:
