from flask import request, Flask, redirect

app = Flask(__name__)


@app.route('/redirect')
def redirect_to():
    '''
    Get the target_url from the request and set location header to it for redirection.
    Ensure that the target_url is not to an external website.
    :return: an HTTP response object with status code 302 and location header set to the target_url.
    '''

#     if not request.args.get('target_url') or request.args.get('target_url').startswith('https://') \
#             or request.args.get('target_url').startswith('http://'):
    if not request.args.get('target_url'):
        return 'Missing target_url argument', 400
#     # remove unwanted characters
#     target_url = re.sub('[\n\r\t\b\a\']', '', request.args.get('target_url'))
#     return redirect(target_url)
    return redirect(request.args.get('target_url'))
    