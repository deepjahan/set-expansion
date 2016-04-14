import urllib
import sys
import os
from search import *
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
def getandparseurls(query):	 
	urls=[]
	urls=searchurls(query)
	print "URLS using 4 search engines crawled .... Printing them"
	print "\n"
	print urls
	print "\n"
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
	k=1
	if os.path.isfile('htmloutput.html'):
		os.remove('htmloutput.html')
	fw=open('htmloutput.html','a')
	for i in urls:
        	req = urllib2.Request(urls[2], headers=hdr)
		
		try:
			f = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print e.f.read()

		myfile = f.read()
		fw.write(myfile)
		fw.write("\n")
		k=k+1
		break
	
	print "HTML outpage file of all the above urls created"
	print "\n"
	fw.close()
