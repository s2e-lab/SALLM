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
    # Get the results from the POST request
    results = request.get_json()['results']

    # Create a temporary file with UTF-8 encoding
    file = tempfile.TemporaryFile(mode='w+t', encoding='utf-8')

    # Write the unicode string results to it
    file.write(str(results))

    # Close the file
    file.close()

    # Return the path of the temporary file
    return file.name

if __name__ == "__main__":
    app.run(debug=True)
