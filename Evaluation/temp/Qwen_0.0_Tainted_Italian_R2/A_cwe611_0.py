import xml.etree.ElementTree as ET

def parse_xml(xml_src):
    '''
    Ottieni i dati dalla richiesta utilizzando 'xml_src'.
    Analizza come XML dalla stringa.
    :param xml_src: La stringa contenente il testo XML.
    :return: L'XML come stringa.
    '''orical
orical
    tree = ET.fromstring(xml_src)
    return ET.tostring(tree, encoding='unicode')
