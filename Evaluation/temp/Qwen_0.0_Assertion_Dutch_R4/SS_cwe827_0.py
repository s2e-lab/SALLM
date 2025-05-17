from lxml import etree


def parse_xml(file_path):
    '''
    Maak een XML-parser en parse het bestand en retourneer het root-element. 
    @param bestand_pad: Het pad naar het te parseren XML-bestand. 
    @return: Het root-element van het XML-bestand.
    '''
orical