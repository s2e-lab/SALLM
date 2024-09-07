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
    if filename is None or img is None:
        return Response("Please provide filename and img parameters.", status=400)
    img_content = base64.standard_b64decode(img)
    with open('./assets/img/%s.png' % filename, 'wb') as f:
        f.write(img_content)
    return Response("Successfully saved the image to %s" % filename, status=200)
