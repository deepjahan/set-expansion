import sys
import urllib2,cookielib
sys.path.append('googlesearch')
from google1 import search
sys.path.append('bing')
from bingsearch import bing_search
sys.path.append('wikisearch')
from wikisearch import wiki_search
sys.path.append('duckduckgo')
from duckduckgosearch import duckduckgo_search

def searchurls(query):
	k=0
	urls=[]
#### Google Search Engine   #####
	buildquery=query.replace(',',' ')
	for url in search(buildquery, stop=10):
		k=k+1
		urls.append(url)
		if k==10:
			break
	print "URLS through google search engine found"
	print "\n"
#### Bing Search Engine    #####
#	bingurls=bing_search(buildquery)
#	urls=urls+bingurls
	print "URLS through bing search engine found"
	print "\n"



#### Wiki Search Engine   #####
#	wikiurls=wiki_search(query)
#	urls=urls+wikiurls
	print "URLS through wikipedia search engine found"
	print "\n"


#### DuckDuck Go Search Engine #####
#	duckduckurls=duckduckgo_search(query)
#	urls=urls+duckduckurls
	print "URLS through duckduckgo search engine found"
	print "\n"

	return urls


##### Main funtion to run the file separately #####

if __name__=='__main__':
	u=[]
	u=searchurls()
	print u
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
#	proxies = {'http': 'http://proxy.iiit.ac.in:8080','https':'https://proxy.iiit.ac.in:8080'}
	for i in u:
		req = urllib2.Request(i, headers=hdr)
		try:
			f = urllib2.urlopen(req)
		except urllib2.HTTPError, e:
			print e.fp.read()
		myfile = f.read()
		print myfile
		break
	
#	fw.close()


	
