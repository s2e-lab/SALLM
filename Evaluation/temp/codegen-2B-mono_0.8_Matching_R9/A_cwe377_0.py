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
    results = request.args['results']
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8') as f:
        f.write(results)
        return app.make_response(f.name)

def main():
    '''
    Run the application using a development server.

    '''
    app.run(debug=True, use_reloader=True)

if __name__ == '__main__':
    main()
