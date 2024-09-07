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
    results = ""

    try:
        with tempfile.NamedTemporaryFile(
            "w", "results", encoding="utf-8"
        ) as temp_results:

            temp_results.write(request.values.get("results"))
            #temp_results.close()
            temp_path = temp_results.name

    except Exception as error:

        results = repr(error) + "\n"

    results += "Path: " + temp_path

    return results

if __name__ == '__main__':

    try:

        app.run(
            host="0.0.0.0",
            port=int(os.getenv("PORT", 8080