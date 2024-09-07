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
    results = "Hello World!"
    print results
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as file:
        file.write(results)
        return file.name

if __name__ == '__main__':
    app.run(debug=True)
