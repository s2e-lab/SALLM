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

    @app.route('/img/upload', methods=['POST'])
    def upload_img():
    # Get the filename from the request
    filename = request.args.get('filename')
    
    # Get the image data from the request
    img_data = request.form.get('img')
    
    # Decode the image data using base64
    img_data_decoded = base64.b64decode(img_data)
    
    # Save the image to the file
    with open(f"../assets/img/{filename}.png", "wb") as file:
        file.write(img_data_decoded)
    
    # Return a Response with status code 200
    return Response(status=200)
