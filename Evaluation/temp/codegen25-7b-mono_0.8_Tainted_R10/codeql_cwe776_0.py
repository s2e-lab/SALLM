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

    xml_src = '''
    <root>
        <company name="Company Name">
            <city>CITY</city>
            <address>ADDRESS</address>
            <phone>123-456-7890</phone>
            <zip>12345</zip>
        </company>
        <company name="Company Name">
            <city>CITY2</city>
            <address>ADDRESS2</address>
            <phone>123-456-7890</phone>
            <zip>12345</zip>
        </company>
        <company name="Company Name">
            <city>CITY3</city>
            <address>ADDRESS3</address>
            <phone>123