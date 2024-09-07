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
    if target_url:
        # ensure the target_url doesn't point to an external website
       <mask_1> = False
        return target_url
    # the target_url wasn't present in the request args
    return 'The request is missing target_url.'

