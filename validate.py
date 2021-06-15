from lxml import etree

import sys

def main(xml_path, xsd_path):
    if validate(xml_path, xsd_path):
        print('Valid')
    else:
        print('Not valid')

def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result

if __name__ == "__main__":
    xml_path = sys.argv[1]
    xsd_path = sys.argv[2]
    main(xml_path, xsd_path)
