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
#    results = request.form.get('results')
    results = request.args.get('results')
    temp_file_path = os.path.join(tempfile.gettempdir(),'temp_file.txt')
    with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        temp_file.write(results)
    return temp_file_path

if __name__ == '__main__':
    app.run(debug=True)
