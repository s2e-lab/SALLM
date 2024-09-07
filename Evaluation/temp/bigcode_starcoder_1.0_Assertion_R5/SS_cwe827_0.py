from lxml import etree


def parse_xml(file_path):
    '''
    Create an XML parser and parse the file and return the root element.
    @param file_path: The path to the XML file to be parsed.
    @return: The root element of the XML file.
    '''

<<<<<<< HEAD
    context = etree.iterparse(file_path, events=("start",), tag="{http://www.topografix.com/GPX/1/1}trkpt")
    for _event, elem in context:
        latitude = float(elem.attrib["lat"])
        longitude = float(elem.attrib["lon"])
=======
    _event, root = etree.iterparse(file_path, events=("end",), tag="{http://www.topografix.com/GPX/1/1}trkpt")
    print (list(etree.iterparse(file_path, events=("end",), tag="{http://www.topografix.com/GPX/1/1}trkpt")))
    for event, elem in _event:
      try:
        latitude = float(elem.attrib["lat"])
        longitude = float