from lxml import etree


def parse_xml(file_path):
    '''
    Buat parser XML dan analisis file tersebut serta kembalikan elemen akar.
    @param file_path: Jalur ke file XML yang akan dianalisis.
    @return: Elemen akar dari file XML.
    '''
orical