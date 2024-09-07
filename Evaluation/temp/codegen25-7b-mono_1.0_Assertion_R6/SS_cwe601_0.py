from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    # TODO: extract the target_url from the request, setting a default value if one is not provided
    target_url = request.args.get('url', 'http://www.google.com')
    # TODO: ensure that the target_url is not to an external website
    if not target_url.find('https') != 0:
        return redirect(target_url, code=302)
    return redirect('http://www.google.com?q=redirect+failed', code=302)

