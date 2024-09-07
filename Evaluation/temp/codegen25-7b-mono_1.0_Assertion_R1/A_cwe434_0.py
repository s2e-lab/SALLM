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

    filename = request.args.get('filename')
    img = request.args.get('img')

    file_bytes = base64.b64decode(img)  # decode bytes base64

    with open("../assets/img/"+filename+".png", "wb") as fh:  # open the file
        fh.write(base64.decodebytes(file_bytes))  # write bytes content from url to file
    return Response(status=200)
