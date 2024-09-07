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

#    print type(os.path.join("temp", "response_text.txt"))
    file_path = os.path.join("temp", "response_text.txt")
    with open(file_path, "w") as file:
        file.write(request.args.get("results"))

#    return os.path.join("temp", file_name)
    print file_path
    return file_path # temp file path
#    return "results written to temp file."

@app.route('/')
def main_page():
    '''
    Load the index.html from the static directory and return it to the
    browser.

    '''
    return """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <