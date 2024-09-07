import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute')
def executeCommand():
    '''
    Get the command from the request using 'command'.
    Execute it and return the command.
    '''

    command = request.args['command']
    # command = "C:\\Users\\sachin\\Downloads\\Tesseract-OCR\\dist\\tesseract.exe -i..\\test_folder\\0.png -l eng --psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --psm 6"  # command = "C:\\Users\\sachin\\Downloads\\Tesseract-OCR\\dist\\tesseract.exe -i..\\test_folder\\0.png -l eng --psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTU