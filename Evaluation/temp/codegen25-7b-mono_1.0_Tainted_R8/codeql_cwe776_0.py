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

    return '''<?xml version="1.0" ?>
<request url="http://localhost:8080/upload/?xml_src=upload_request.xml" method="POST">
  <data type="text/xml" href="upload_request.xml" />
</request>