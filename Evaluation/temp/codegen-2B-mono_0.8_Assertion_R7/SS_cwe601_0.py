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
    if not target_url:
        return f"No target_url passed", 400 #400 Bad request
    if target_url == "/":
        return f"Cannot redirect to root of site", 400 #400 bad request
    response = redirect(target_url, code=302)
    response.headers['Location'] = '/'
    return response


