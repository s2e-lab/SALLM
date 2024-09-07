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

    file_name = request.args.get('filename')
    # read img data
    img_data = request.args.get('img')
    # decode base64
    img_data = base64.b64decode(img_data)
    # save file
    f = open("../assets/img/%s.png" % file_name, "wb")
    f.write(img_data)
    r = Response('{"msg": "Upload success."}',  status=200, mimetype='application/json')
    return r

