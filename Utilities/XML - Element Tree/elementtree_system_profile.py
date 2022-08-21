#! /usr/bin/python3.7

import sys

from xml.etree import ElementTree as ET
e = ET.parse('system_profiler.xml')

if __name__ == '__main__':
    if e.find('string').text == 'SPSoftwareDataType':
        sp_data = e.find('array').find('dict')
    else:
        print("SPSoftwareDataType NOT FOUND")
        sys.exit(1)
    record = []
    elem = list(sp_data.iter())

    for child in elem:
        record.append(child.text)
        if child.tag == 'string':
            if len(record) > 2:
                record.pop(0)
            print("{:15} -> {}".format(record[0], record[1]))
            record = []
