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
    #     URL=request.args.get('url')
    #     url = URL
    #     if not URL:
    #         raise NameError('No URL was found')
    #     else:
        url=request.args.get('url').strip()
    except NameError as e:
        print('Error occurred')
        return e
    file = open('temp.tmp', 'wb+')
    print('file created')
    resp = requests.get(url)
    print(resp)
    file.write(resp.content)
    print('downloaded')
    file.close()
    return url

