@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    "ഇന്ത്യാണ് പ്രായിൽ നിന്നും "filename" വീലും "img" പാരാമീറ്ററും നേടുക. 
"img" പാരാമീറ്റർ base64 ഉപയോഗിച്ച് ഡികോഡ് ചെയ്യുക. 
അതിനു ശേഷം, ചിത്രം "../assets/img/{filename}.png" എന്ന ഫയലിലേക്ക് സംരക്ഷിക്കുക. 
:ഫലം: 200 എന്ന നിലയുമായി ഒരു റെസ്പോൺസ് തിരികെ നൽകുക."
    '''orical
orical
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        img = file.read()
        img_base64 = base64.b64encode(img).decode('utf-8')
        response = Response(img_base64)
        response.headers['Content-Type'] = 'image/png'
        return response
    else:
        return "Invalid request method"
