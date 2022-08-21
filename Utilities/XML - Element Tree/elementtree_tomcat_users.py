#! /usr/bin/python3.7

from xml.etree import ElementTree as ET

if __name__ == '__main__':
    infile = 'apacheUser.xml'
    tomct_users = ET.parse(infile)
    for user in [e for e in tomct_users.findall('./user') if e.get('name') == 'tomcat']:
        print(user.attrib)
