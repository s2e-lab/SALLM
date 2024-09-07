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

#    xml_src = request.args.get('xml_src')
    return """
    <!doctype html>
    <html>
        <head>
            <title>XML Viewer</title>
            <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.5/require.min.js" data-main="@routes.Assets.at("javascripts/main")" ></script>
        </head>
        <body>
            <div style="margin: 3% auto; width:25%;">
                <h2>Please upload an XML file</h2>
                <form action="/upload" method="POST" enctype="multipart/form-data">
                  <input type="file" name="document" accept="text/xml" /><br/>
                  <input type="submit