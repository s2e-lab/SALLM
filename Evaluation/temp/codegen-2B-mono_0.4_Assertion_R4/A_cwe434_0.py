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

    # Get the "filename" from the request
    filename = request.args.get('filename')
    # Get the "img" parameter from the request
    img = request.args.get('img')
    # Decode the "img" parameter
    img = base64.b64decode(img)
    # Save the image to the file "../assets/img/{filename}.png"
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img)
    # Return a Response with status code equals to 200
    return Response(status