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

    xml_src = request.args.get('xml_src')
    data = xml_src.encode('utf-8')
    # Create the XML tree
    tree = ET.fromstring(data)
    #print(tree)
    # Get the root element
    root = tree.getchildren()[0]
    #print(root)
    # Get the child elements of the root
    child = root.getchildren()
    #print(child)
    # Get the child elements of the child
    children = child[0].getchildren()
    #print(children)
    # Get the child elements of the children
    child1 = children[0].getchildren()
    #print(child1)
    # Get the