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

# +++your code here+++
# Write the results from the request to a temporary file
# and pass its path to the client.
    results = request.args.get('results')
    tmp_file = tempfile.TemporaryFile(mode='w+t')
    tmp_file.write(results)
    tmp_file.close()
    return jsonify({'file_path':tmp_file.name})

# An example of running your function locally.
# Note that `port=5001` is used because this is the port 
# configured in `config.py`
#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=5001, debug=True)
