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

#    results = request.args.get('results')
    results = request.args.get('results')
    print(results)
    print(type(results))
    print(results.encode('utf-8'))
    print(type(results.encode('utf-8')))
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(results.encode('utf-8'))
    return temp.name

if __name__ == '__main__':
    app.run(debug=True)
