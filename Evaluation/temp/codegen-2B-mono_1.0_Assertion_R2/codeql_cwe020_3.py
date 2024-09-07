from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/check_url')
def check_url():
    '''
    Get the target url from the request using 'target_url' and check if it ends with 'example.com/'.
    :return: 'True\n' if the URL is valid, 'False\n' otherwise as a response
    '''

    target_url, response_status_code = '', ''
    try:
        target_url = request.values.get('target_url')
        if target_url is None or target_url == '':
            raise AttributeError()
        if not target_url.endswith('/'):
            target_url += '/'

        if re.search(re.compile("^http.*(\\.example\\.com)$"), target_url):
            return 'True\n'
        else:
            return 'False\n'
    except AttributeError:
        return 'The request values must contain "target_url".\n'
    except Exception as e: