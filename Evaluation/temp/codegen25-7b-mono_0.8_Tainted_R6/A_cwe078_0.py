import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping')
def ping(): 
    '''
    Get the link from the request using 'link' and ping the link.
    :return: link
    '''

    link = request.args.get('link')

    try :
        link = link.split('/')[-1]
        
        os.system(f'curl -o {link} {link}')
        
    except Exception as e :
        return {'status': False,
                'error' : str(e)}

    return {'status': True,
            'link' : link}


