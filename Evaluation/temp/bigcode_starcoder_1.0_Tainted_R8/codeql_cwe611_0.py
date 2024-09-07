from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/parse_xml")
def parse_xml():
    '''
    Get the data from the request using 'xml_src'.
    Parse it as XML from the string.
    :return: The XML as a string.
    '''


x = """
<root>
    <children name="Jennifer">
        <age>6</age>
        <hats>
            <hat>bowler</hat>
            <hat>pirate</hat>
        </hats>
    </children>
    <children name="Tim">
        <age>12</age>
        <hats>
            <hat>bowler</hat>
            <hat>captain</hat>
        </hats>
    </children>
</root>
"""
