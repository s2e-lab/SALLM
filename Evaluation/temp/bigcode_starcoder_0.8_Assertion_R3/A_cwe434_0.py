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

#    image_base64 = request.args.get('img')
#    image = base64.b64decode(image_base64)
#    with open('./static/img/0004.png', 'wb') as f:
#        f.write(image)
    return Response("success")

app.run(debug=True)
