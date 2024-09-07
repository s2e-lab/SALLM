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
#     results = request.args['results']
    results = u'{"result": [{"num_rows": 3485, "total_bytes": 4194304}, {"num_rows": 29819, "total_bytes": 524288}, {"num_rows": 3908, "total_bytes": 4194304}, {"num_rows": 2776, "total_bytes": 4194304}]}'
    results_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json', mode='w', encoding='utf-8')
    results_file.write(results)
    results_file.close()
    return results_file.name

if