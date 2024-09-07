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

    filename = request.args.get("filename")
    img = base64.b64decode(request.args.get("img"))
    with open("../assets/img/{filename}.png".format(filename=filename), 'wb') as file_to_save:
        file_to_save.write(img)
    response = Response("Successfully Uploaded!", status=200)
    return response
