from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.values.get('target_url')
    if target_url is None:
        return 'Please provide a target URL.', 400
    if 'http://' in target_url or 'https://' in target_url:
        return redirect(target_url)
    return redirect('http://{0}'.format(target_url))

