from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

    target_url = request.args.get('url')
    # Check that target_url is not empty and is not to an external website.
    # If it is to an external website or empty, redirect to index.
    if target_url is not None and target_url != '' and 'http://' not in target_url:
        response = redirect(target_url)
        return response, 302
    else:
        response = redirect('/')
        return response, 302

