# -*- coding: utf-8 -*-
import sys
sys.path.append('word2vec')
sys.path.append('PatternRecognition')
sys.path.append('outputFiles')
sys.path.append('Crawling')
sys.path.append('API/googlesearch')
sys.path.append('API/bing')
sys.path.append('API/faroo.py-master')
sys.path.append('API/wikisearch')
from HTMLParser import HTMLParser
import re
from nltk.stem.porter import *
from nltk.corpus import stopwords
from getpage import getandparseurls
import os  
from compare import find_similarity
cachedStopWords = []
for i in stopwords.words("english"):
	cachedStopWords.append(i.encode('utf-8'))
lst=[]
isscript=False
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
	
	def handle_starttag(self, tag, attrs):
		global isscript
		isscript=False
#		print tag
		if tag=='script':
#print 'ignor'
			isscript=True
		pass
#print "Encountered a start tag:", tag
	def handle_endtag(self, tag):
		pass
#print "Encountered an end tag :", tag
	def handle_data(self, data):
		global isscript
		global lst
		if not isscript:
			cnt=re.sub("[~`!@#$%^&*()_-]",' ',data) 
			cnt=re.sub("[+={}\[\]:>;]",' ',cnt) 
			cnt=re.sub("[',</?*+|\\\".]",' ',cnt)
			cnt=cnt.split()
			for i in cnt:
				try:
					if i.isalnum():
						if i.encode('utf-8') not in cachedStopWords:
							lst.append(i.encode('utf-8'))
				except:
					pass
		isscript=False	

getandparseurls(sys.argv[1])
parser =MyHTMLParser()
f=open('outputfiles/htmloutput.html','r')
print "Parsing and getting all the tokens from the html output file\n"
data=f.read()
try:
	data=data.decode('utf-8')
except:
	pass
parser.feed(data)
lst=set(lst)
#stemm = PorterStemmer()
#lst=[stemm.stem(word).encode('utf-8') for word in lst]
#print len(lst)
if os.path.isfile("outputfiles/indexfile"):
	os.remove("outputfiles/indexfile")
fw=open("outputfiles/indexfile",'w')
print "Writing all the tokens to a indexfile"
for i in lst:
	fw.write(str(i))
	fw.write("\n")

fw.close()
f.close()
find_similarity(sys.argv[1])

