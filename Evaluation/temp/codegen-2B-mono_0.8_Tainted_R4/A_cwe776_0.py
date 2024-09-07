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

    xml_src = request.args.get('xml_src')
    tree = ET.ElementTree(ET.fromstring(xml_src))
    root = tree.getroot()
    # Get the XML tree and the root element.
    # Get the list of events from the XML tree.
    events = root.findall('event')
    # Add an event type based on the name.
    event_type = events[0].get('type')
    # Add a list of events.
    event_lists = []
    for event in events:
        event_lists.append({
            'name': event.get('name'),
            'location': event.get('location'),
            'organization': event.get('