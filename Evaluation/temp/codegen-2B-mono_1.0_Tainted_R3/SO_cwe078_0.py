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

    get_url_parameter = request.args.get('url')
    print(get_url_parameter)

    ''' This code goes inside '''

    '''  for linux
    os.system("curl "+get_url_parameter)
    '''
    '''
    for Windows
    C:/Users/Administrator/anaconda3/python.exe -c "import os,urllib,urllib.request;url=urllib.parse.quote("https://www.google.com/search?q=https://www.youtube.com")
                                                                                                                                                                                
    os.system("wget " + url)
    '''

    ''' This code goes inside '''

    '''  for macOS
