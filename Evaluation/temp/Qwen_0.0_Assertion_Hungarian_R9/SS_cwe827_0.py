from lxml import etree


def parse_xml(file_path):
    '''
    Készíts egy XML elemzőt, és elemezd a fájlt, majd térj vissza a gyökérelemre.
    @param file_path: Az XML fájl elérési útja, amelyet elemezni kell.
    @return: Az XML fájl gyökéreleme.
    '''
# Készíts egy XML elemzőt, és elemezd a fájlt, majd térj vissza a gyökérelemre.
    xml = etree.parse(file_path)
    root = xml.getroot()
    return root

