import logging
from flask import Flask, request


app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Log data from request and return it.
    '''

    try:
        # Get data from request and log in log_file.
        data = request.get_json()

        # Create log_file.
        log_file = open("log_file.txt", "a")
        log_file.write("\n")

        # Write data to log_file.
        log_file.write("Data From Request: ")
        log_file.write("\n")
        log_file.write(str(data))
        log_file.write("\n")

        # Close log_file.
        log_file.close()

        # Return data.
        return data, 200
    except:
        return "Something went wrong!", 500

