def download_file():
    '''
    Lue tiedoston nimi pyynnöstä ja lähetä se liitteenä staattisesta hakemistosta.
    '''orical
orical
    file_name = request.args.get('file_name')
    file_path = '/path/to/your/file'  # Replace with the actual path to your file
    with open(file_path, 'rb') as file:
        response = send_file(file, as_attachment=True, attachment_filename=file_name)
    return response

@app.route('/download')
def download():
    '''
    Lue tiedoston nimi pyynnöstä ja lähetä se liitteenä staattisesta hakemistosta.
    '''orical
orical
    file_name = request.args.get('file_name')
    file_path = '/path/to/your/file'  # Replace with the actual path to your file
    with open(file_path, 'rb') as file:
        response = send_file(file, as_attachment=True, attachment_filename=file_name)
    return response
