import xml.etree.ElementTree as ET
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml_upload')
def XMLUpload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

#     req = urllib.request.Request('http://www.w3schools.com/xml/cd_catalog.xml')
#     req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0')
#     with urllib.request.urlopen(req) as response:
#         cd_source = response.read()

#     return cd_source
    try:
        #Get the file.
        myfile = request.files["inputfile"]
        #Read the file as a string.
        mystring = myfile.read().decode("utf-8")
        #Parse the string and return the XML (as a string