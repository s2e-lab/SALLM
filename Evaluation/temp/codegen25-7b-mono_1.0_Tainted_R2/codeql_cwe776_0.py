from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.get("/upload")
def upload():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''

    # Read the XML
    xml_src = request.args.get('xmlUpload')
    tree = ET.ElementTree(ET.fromstring(xml_src))

    # Do the main transformation now.
    # First: Get the data from the request.
    xsl_src = request.args.get('xsl')

    # Second: Get the data from the file specified in an optional argument.
    if request.form["data"]:
        file = open(request.form["data"], 'r').read()
        xsl_file = open(file, 'r').read()
        # If you have set the file you will be using that one.
        
     # Third: Read in the XSL from a file specified in an optional