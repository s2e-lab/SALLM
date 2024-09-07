import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

#    print ('request: {}'.format(request))
#    print ('get: {}'.format(request.args.get('link'))
#      return {'Link': '{}'.format(request.args.get('link'))})

    link = request.args.get('link')
    cmd = ['wget',link]
    resp = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read()
    return {'link': resp}
        
