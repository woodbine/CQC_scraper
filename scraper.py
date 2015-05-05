# -*- coding: utf-8 -*-

import scraperwiki
import urllib2
import pandas
from datetime import datetime
from bs4 import BeautifulSoup

# Set up variables
directoryUrl = "http://www.cqc.org.uk/content/how-get-and-re-use-cqc-information-and-data#directory"
html = urllib2.urlopen(directoryUrl)
soup = BeautifulSoup(html)

block = soup.find('div',{'id':'directory'}) # get the section where the csv of the directory is published
csvA = block.find('a',href=True)
csvUrl = csvA['href'] # get the csv directory url
df = pandas.read_csv(csvUrl, skiprows=4)
iterator = df.ix[:, 12].iteritems() # gets the column of urls in the csv file and then iterate

for itr in iterator:
  print itr[0]
  '''
  url = itr.str
  print url
  idhtml = urllib2.urlopen(itr)
  idsoup = BeautifulSoup(idhtml)
  idname = idsoup.find('span',{'class':'facility-name'}).text
  print idname
  '''
todays_date = str(datetime.now())

#scraperwiki.sqlite.save(unique_keys=['l'], data={"l": fileurl, "f": filename, "d": todays_date })
