# -*- coding: utf-8 -*-

__author__ = 'RadyHuang'

import urllib2,xml.dom.minidom
from os.path import expanduser

home = expanduser("~")

theQuery = u"{query}"

doc = xml.dom.minidom.parse( home +'/.filezilla/sitemanager.xml')

print "<?xml version=\"1.0\"?>\n<items>"
for item in doc.getElementsByTagName('Server'):
    title = item.getElementsByTagName('Name')[0].firstChild.data
    line  = title.replace('.','\.')   

    if(title.__contains__(theQuery)) or theQuery == "": 
       print "    <item uid=\"filezilla\" arg=\""+ line +"\">"
       print "        <title>" + title.encode('utf-8') + "</title>"
       print "        <subtitle>Open " + title.encode('utf-8') + " in Open in Filezilla</subtitle>"
       print '''        <icon type="fileicon">/Applications/Filezilla.app</icon></item>'''
       
print "</items>\n"