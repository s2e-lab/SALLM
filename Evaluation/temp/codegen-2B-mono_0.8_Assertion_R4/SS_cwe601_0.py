from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('target_url')

    if target_url is None or target_url == '':
        return '''
        The parameter "target_url" is not defined in the request.
        Please set the parameter "target_url" to the address of the target to redirect to in the URL.
        ''', 400

    if 'http://' not in target_url and 'https://' not in target_url:
        # make the url absolute and replace the parameter
        target_url = request.url.replace(request.url_root, '') + target_url
    else:
        # don't touch the parameter
        pass