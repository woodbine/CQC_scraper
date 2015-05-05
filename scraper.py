# -*- coding: utf-8 -*-

import scraperwiki
import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup

# Set up variables
directoryUrl = "http://www.cqc.org.uk/content/how-get-and-re-use-cqc-information-and-data#directory"
html = urllib2.urlopen(directoryUrl)
soup = BeautifulSoup(html)

block = find('div',{'id':'directory'})
csvA = find('a',href=True)
csvUrl = csvA['href']

print csvUrl



todays_date = str(datetime.now())

#scraperwiki.sqlite.save(unique_keys=['l'], data={"l": fileurl, "f": filename, "d": todays_date })
