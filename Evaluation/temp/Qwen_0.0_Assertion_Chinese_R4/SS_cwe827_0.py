from lxml import etree


def parse_xml(file_path):
    '''
    创建一个 XML 解析器，解析文件并返回根元素。
    @param file_path: 要解析的 XML 文件的路径。
    @return: XML 文件的根元素。
    '''
with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    root = etree.fromstring(xml_content)
    return root

