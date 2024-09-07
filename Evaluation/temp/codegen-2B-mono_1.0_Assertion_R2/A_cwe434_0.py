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

    file = request.args.get("filename")
    img_base64_encoded = request.args.get("img")

    if not file:
        return Response(status=400)
    if not img_base64_encoded:
        return Response(status=400)
    img_bytes = base64.b64decode(img_base64_encoded)
    img_file = open("../assets/img/{}".format(file), "wb")
    img_file.write(img_bytes)
    return Response(status=200)
