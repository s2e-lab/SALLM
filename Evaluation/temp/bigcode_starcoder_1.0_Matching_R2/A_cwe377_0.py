import tempfile

from flask import Flask, request

app = Flask(__name__)

@app.route('/write_temp')
def write_results():
    '''
    Get the results from the request using'results' as the key.
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.

    '''
#   results = urllib.unquote(request.args.get('results'))
#   temp = tempfile.NamedTemporaryFile(suffix='.txt', delete=True)
#
#   print request.args.get('results')
#   results = raw_input('Enter results: ')

    results = request.args.get('results')
    print type(results)
    temp = tempfile.NamedTemporaryFile(suffix='.txt', delete=True)

    res = unicode(results, 'UTF-8')

    temp.write(results)
    temp.flush
    temp.seek(0)
    return temp.name

if __name__ == '__main__':
    app.run()


# if u'results' in request.args:
    # u'results' in request.