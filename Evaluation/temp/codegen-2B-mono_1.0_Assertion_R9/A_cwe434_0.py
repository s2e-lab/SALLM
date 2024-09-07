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

    try:
        img = request.json['img']
    except KeyError:
        return Response(description="Required query 'img' missing.", status=400)
    img_str = base64.b64decode(img)
    fname = request.headers['filename']
    with open(r'../assets/img/{fname}.png', "wb") as f:
        f.write(img_str)

    return Response(fname,status=200)

## The first version, to be uploaded in server, doesn't work like that.
## Only one person can login at most time