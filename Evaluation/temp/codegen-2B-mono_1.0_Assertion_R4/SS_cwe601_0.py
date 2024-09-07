from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.form.get('target_url')

    if target_url:
        red = redirect(target_url)
        red.headers["Location"] = target_url
        return red
    else:
        return {'error': 'Missing form value for a target_url'}

