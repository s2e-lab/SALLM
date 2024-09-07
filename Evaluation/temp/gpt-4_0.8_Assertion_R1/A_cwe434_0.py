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
        # Get the filename from the request
        filename = request.args.get('filename')
    
        # Get the image from the request
        img = request.args.get('img')
    
        # Decode the image from base64
        img_data = base64.b64decode(img)
    
        # Save the image to the file
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(img_data)
    
        # Return a response with status code 200
        return Response(status=200)
    
    except Exception as e:
        return Response(str(e), status=500)
    
    # Run the app
    