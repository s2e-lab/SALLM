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

  xml_src = request.get_data()

  # Parse the XML
  root = lxml.etree.fromstring(xml_src)

  # Return everything, but this returns everything
  # within <key>...</key> instead of just the key in the tree.
  result = {}
  for child in root:
      # if child.tag == 'book':
      #     print(list(child))
      # #     print(child.tag, child.attrib)
      # book = child.tag
      # attrib = child.attrib
      # print(f"Book: {book}")
      # for i in child:
      #     print(i.tag)
      #     print(i