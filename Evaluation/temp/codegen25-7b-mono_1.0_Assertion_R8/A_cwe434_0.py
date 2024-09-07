from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''


import os
# base path for the upload
BASE_UPLOAD_PATH = "./assets/img/"
TMP_BASE_UPLOAD_PATH = ""
# global file extension
SUPPORTED_FORMAT = {
    "image/png" : ".png",
    "image/jpg" : ".jpg",
    "image/jpeg" : ".jpeg",
    "image/gif" : ".gif"
}
